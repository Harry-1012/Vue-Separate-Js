
import os

# python3
# Vue-Separate-Js Vue分离JS文件

def get_filelist(dir):
    fileList = []
    for parent, dirnames, filenames in os.walk(dir,  followlinks=True):
        for filename in filenames:
            file_path = os.path.join(parent, filename)
            if filename.find('.vue') >= 0:
              fileList.append({
                  'name': filename,
                  'dir': file_path
              })
    modifyFile(fileList,0)

def modifyFile(fileList,index):        
    currentFile = fileList[index];
    print('文件：%s' % currentFile)
    with open(currentFile['dir'],'r', encoding='UTF-8') as file_obj:
      content = file_obj.read()
      scriptContent = (content[content.find('<script>')+8:content.find('</script>')])
      # JS file name
      jsFileName = currentFile['name'].replace('.vue','.js')
      # other way import * ... export 
      newVueScript = '\nimport js from "./'+jsFileName+'";\nexport default js;\n'
      # replace old script 
      newVueContent = content.replace(scriptContent,newVueScript)
      # rewrite old vue file
      file_obj.close()

    # replace old vue file
    with open(currentFile['dir'],'w', encoding='UTF-8') as new_vue_file:
      new_vue_file.write(newVueContent)
      new_vue_file.close()

    # new a js file  
    with open(currentFile['dir'].replace('.vue','.js'),'w', encoding='UTF-8') as js_obj:
      js_obj.write(scriptContent)
      js_obj.close()
    if index < (len(fileList)-1):
        modifyFile(fileList,index+1)
    else:
        print('success,all '+ str(index+1)+'`s files')      
     
if __name__ == "__main__":
    get_filelist('dist/')
    