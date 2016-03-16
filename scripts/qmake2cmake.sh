#!/usr/bin/ruby -w

# Get the file into a string
file = IO.read(ARGV[0]);

# Convert special qmake variables
projectName = String.new;
file.sub!(/TARGET = (.+)$/) {
    projectName = $1.dup;
    "PROJECT(#{projectName})"
}
templateType = String.new;  # We remove the project type and stick it at the end
file.sub!(/TEMPLATE = (.+)$\n/) {
    templateType = $1.dup;
    ""
}
file.gsub!(/include\((.+)\)/,
           'INCLUDE(\1 OPTIONAL)');
file.gsub!(/includeforce\((.+)\)/,
           'INCLUDE(\1)');
file.gsub!(/INCLUDEPATH \*= (.+)((\n[ \t]+.+$)*)/,
           'SET(CMAKE_INCLUDE_PATH ${CMAKE_INCLUDE_PATH} \1\2)');
file.gsub!(/SOURCES \*= (.+)((\n[ \t]+.+$)*)/,
           "SET(#{projectName}_sources $#{projectName}_sources" ' \1\2)');
file.gsub!(/HEADERS \*= (.+)((\n[ \t]+.+$)*)/,
           "SET(#{projectName}_headers $#{projectName}_headers" ' \1\2)');
file.gsub!(/DEFINES \*= (.+)((\n[ \t]+.+$)*)/,
           'SET(DEFINES ${DEFINES} \1\2)');

# Now deal with other variables
file.gsub!(/(.+)\s\*=\s(.+)/,
           'SET(\1 ${\1} \2)');
file.gsub!(/(.+)\s=\s(.+)/,
           'SET(\1 \2)');
file.gsub!(/\$\$\{(.+)\}/,
           '${\1}');
file.gsub!(/\$\$\((.+)\)/,
           '$ENV{\1}');
file.gsub!(/([A-Za-z_\-.]+)\.pri/,
           '\1.cmake');

# Cleanup steps
file.gsub!(/\\\)/, ')');

# Put the project type back in
file += "ADD_EXECUTABLE(#{projectName} #{projectName}_sources)" if templateType == "app";
file += "ADD_LIBRARY(#{projectName} ${#{projectName}_sources})" if templateType == "lib";

# Write the new file to CMakeLists.txt
if ARGV.length > 1
    outname = ARGV[1];
else
    if ARGV[0] =~ /.+\.pro$/
        outname = File.join(File.dirname(ARGV[0]), "CMakeLists.txt");
    elsif (ARGV[0] =~ /.+\.pri$/) || (ARGV[0] =~ /.+\.prf$/)
        outbase = File.basename(ARGV[0]);
        outbase.sub!(/\.pr./, ".cmake");
        outname = File.join(File.dirname(ARGV[0]), outbase)
    end
end
outfile = File.new(outname, "w");
outfile.puts(file);
outfile.close;
