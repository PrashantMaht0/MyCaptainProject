name = input("Input the Filename: ")
f_extns = name.split(".")

r_extns=repr(f_extns[-1])
print("The extension of file is :"+ r_extns)
