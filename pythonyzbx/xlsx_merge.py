import sys
import pandas as pd
import glob

def pd_excel(in_file='in.xlsx'):
#    xls = pd.ExcelFile(in_file)
    df1 = pd.read_excel(in_file, 'Sheet1', skiprows=[0])
    df2 = pd.read_excel(in_file, 'Sheet2', skiprows=[0])
    df3 = pd.read_excel(in_file, 'Sheet3', skiprows=[0])
    return df1,df2,df3
    
# runs the csv_from_excel function:
if __name__ == '__main__':
    files=glob.glob('excels/*.xlsx')
    print(len(files),files)
    
    for idx,f in enumerate(files):
        df1,df2,df3=pd_excel(f)
        if idx==0:
            df1_merge=df1
            df2_merge=df2
            df3_merge=df3
        else:
            df1_merge=pd.concat([df1_merge,df1],ignore_index=True)  
            df2_merge=pd.concat([df2_merge,df2],ignore_index=True) 
            df3_merge=pd.concat([df3_merge,df3],ignore_index=True) 
    
    cols=['学院','专业班级','姓名','性别','学号','入团年龄','联系电话']
    print('sheet 1'+'*'*30)
    print(df1_merge.sort_values('学号')[cols])
    print('sheet 2'+'*'*30)
    print(df2_merge.sort_values('学号')[cols])
    print('sheet 3'+'*'*30)
    print(df3_merge.sort_values('学号')[cols])    
        
    print('merge all'+'*'*30)
    df_all=pd.concat([df1_merge,df2_merge,df3_merge],ignore_index=True)
    print(df_all.sort_values('姓名')[cols])
    
    with pd.ExcelWriter('concat.xlsx') as writer:
        df1_merge[cols].to_excel(writer, sheet_name='Sheet1')
        df2_merge[cols].to_excel(writer, sheet_name='Sheet2')
        df3_merge[cols].to_excel(writer, sheet_name='Sheet3')
        df_all.sort_values('姓名')[cols].to_excel(writer, sheet_name='all')
    