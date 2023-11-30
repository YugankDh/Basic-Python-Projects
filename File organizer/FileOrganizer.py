import os 
import shutil

path = input("Enter The Path:")
files = os.listdir(path)

video = ['mp4','avi','mpg','mov','webm']
audio = ['mp3','aac','mpa']
document = ['pdf','doc','html','xls']
image = ['jpg','jpeg','ico','png','svg','bmp']

for file in files:
	file_path = os.path.join(path,file)
	if os.path.isfile(file_path):

		filename,extension = os.path.splitext(file)
		extension = extension[1:]

		if extension in video:
			if os.path.exists(path+'/'+'Video'):
				shutil.move(path+'/'+file,path+'/'+'Video')
			else:
				os.makedirs(path+'/'+'Video')
				shutil.move(path+'/'+file,path+'/'+'Video')

		elif extension in audio:
			if os.path.exists(path+'/'+'Audio'):
				shutil.move(path+'/'+file,path+'/'+'Audio')
			else:
				os.makedirs(path+'/'+'Audio')
				shutil.move(path+'/'+file,path+'/'+'Audio')
		elif extension in document:
			if os.path.exists(path+'/'+'Documents'):
				shutil.move(path+'/'+file,path+'/'+'Documents')
			else:
				os.makedirs(path+'/'+'Documents')
				shutil.move(path+'/'+file,path+'/'+'Documents')
		elif extension in image:
			if os.path.exists(path+'/'+'images'):
				shutil.move(path+'/'+file,path+'/'+'images')
			else:
				os.makedirs(path+'/'+'images')
				shutil.move(path+'/'+file,path+'/'+'images')

		else:
			if os.path.exists(path+'/'+'others'):
				shutil.move(path+'/'+file,path+'/'+'others')
			else:
				os.makedirs(path+'/'+'others')
				shutil.move(path+'/'+file,path+'/'+'others')

