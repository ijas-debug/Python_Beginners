import module_sam

# from module_sam import checkNeg #to call a function
# import module_sam as ifs ->to rename module
# from module_sam import checkNeg as check ->rename function

# print(__name__)  # to know which module currently we are
print(module_sam.__name__)
module_sam.checkNeg(10)

# check=module_sam.checkNeg

# check(10) #we can also call like this
