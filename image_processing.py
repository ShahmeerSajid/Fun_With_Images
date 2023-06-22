#Name : Shahmeer Sajid
#Student ID : 261073334

#Question1: Fun with Images (100 Points)

import doctest
def is_valid_image(list1):
    '''
    (list<list<int>>) --> bool
    
    This function takes a nested list as input
    and returns True if the nested list represents
    a valid non-compressed PGM image matrix.
    Otherwise it returns False.
    A valid PGM image matrix contains 'integers'
    between 0 and 255 and the length of each
    matrix row is the same.
    
    >>> is_valid_image([[1,2,3], [4,5,6], [7,8,9]])
    True
    >>> is_valid_image([[1,2,3000],[2,2,255],[9,9,9]])
    False
    >>> is_valid_image([['9'],[200],[255]])
    False
    >>> is_valid_image([[-1],[200],[255]])
    False
    '''
    length=len(list1[0])
    for i in range(0,len(list1)):
        if len(list1[i])!=length:
            return False
        for j in range(0,len(list1[i])):
            element=list1[i][j]
            if type(element)!=int or element<0 or element>255:
                return False
    return True

def is_valid_compressed_image(list1):
    '''
    (list<list<str>>) --> bool
    This function takes a nested list as input and returns
    True if the nesed list represents a valid compressed PGM
    image matrix; otherwise, it returns False.
    
    A compressed PGM image matrix is valid if it contains strings
    of form 'AxB', where A is an integer between 0 and 255 and B is
    a positive integer. The sum of all B values of each inner-
    list must also be the same.
    
    >>> is_valid_compressed_image([["0x5", "200x2"], ["111x7"]])
    True
    >>> is_valid_compressed_image([["200x10"],["100x10"],["10x10"]])
    True
    >>> is_valid_compressed_image([["212x4", "200x1","123x1"],["111x6"]])
    True
    >>> is_valid_compressed_image([["500x5","100xa"],["110x2"]])
    False
    >>> is_valid_compressed_image([["0x1","100x-1"],["0x2"]])
    False
    >>> is_valid_compressed_image([["-1x15"],["100x15"],["x8"],["80x7"]])
    False
    '''
    # def is_digit(string):
    #     for i in range(0,len(string)):
    #         if string[i] not in ['0','1','2','3','4','5','6','7','8','9']:
    #             return False
    #     return True
    
    sum_array=[] #would contain sum of all B elements...
    for i in range(0,len(list1)):
        sum = 0
        for j in range(0,len(list1[i])):
            element=list1[i][j]
            if (type(element)!=str)or('x' not in element):
                return False
            x_index = element.find('x')
            A = element[0:x_index]
            B = element[x_index+1:]
            # Ensuring that A and B do not contain alphabets and decimals...
            if  not A.isdigit() or not (int(A)>=0 and int(A)<=255) or not B.isdigit() or int(B)<=0:
                return False
            sum += int(B)
        sum_array.append(sum)
    for i in range(0,len(sum_array)-1):
        if sum_array[i]!=sum_array[i+1]:
            return False
    return True


def load_regular_image(file_name):
    '''
    (str)-->(list<list<int>>)
    This function takes a filename as input and checks its validity that
    is it a valid pgm image or not. If it is a valid PGM image, it returns
    the image matrix, otherwise an assertion error is raised.
    
    >>> load_regular_image("comp.pgm")
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    >>> fobj = open("valid_test3.1.pgm",'w')
    >>> fobj.write("P2\\n24 7\\n255\\n0 0 0 0 0 0 0 0 0\\n0 51 30 20 10 10 20 25 35")
    55
    >>> fobj.close()
    >>> load_regular_image("valid_test3.1.pgm")
    [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 51, 30, 20, 10, 10, 20, 25, 35]]
    
    >>> fobj = open("invalid_test3.1.pgm",'w')
    >>> fobj.write("P2\\n24 7\\n255\\n0 0 0 0 0 0 a\\n10 12 15 13 12 13 45")
    46
    >>> fobj.close()
    >>> load_regular_image('invalid_test3.1.pgm')
    Traceback (most recent call last):
    AssertionError: The image should be in "PGM format"...
    '''
    fobj = open(file_name,'r')
    pixel_list1=[]
    for line in fobj:

        array=line.strip().split()
        for i in range(0,len(array)):
            if array[i].isdecimal():
                array[i] = int(array[i])
        pixel_list1.append(array)
    
    fobj.close()
    pixel_list1=pixel_list1[3:]
    
    if len(pixel_list1)==0 or not is_valid_image(pixel_list1):
        raise AssertionError('The image should be in "PGM format"...')
    return((pixel_list1))
    
def load_compressed_image(file_name):
    '''
    (str) --> (list<list<str>>)
    This function takes a filename of a compressed PGM image file and
    loads in the image contained in the file and returns it as a
    compressed image matrix.
    If the image matrix is not in compressed PGM format, then an
    AssertionError with an appropriate error message is raised.
    
    >>> load_compressed_image('comp.pgm.compressed')
    [['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]
    
    >>> fobj = open("valid_test4.1.pgm","w")
    >>> fobj.write("P2C\\n30 5\\n255\\n3x23 0x7\\n5x30")
    26
    >>> fobj.close()
    >>> load_compressed_image("valid_test4.1.pgm")
    [['3x23', '0x7'], ['5x30']]
    
    >>> fobj = open("invalid_test4.2.pgm","w")
    >>> fobj.write("P2C\\n30 10\\n255\\n0x24\\n3x14 5x12 7x10\\n10x12 14x25 10x10")
    51
    >>> fobj.close()
    >>> load_compressed_image("invalid_test4.2.pgm")
    Traceback (most recent call last):
    AssertionError: The image must be in "compressed PGM format"...
    '''
    fobj = open(file_name,'r')
    pixel_list1=[]
    for line in fobj:
        array = line.strip().split()
        pixel_list1.append(array)
    pixel_list1=pixel_list1[3:]
    fobj.close()
    
    if len(pixel_list1)==0 or not is_valid_compressed_image(pixel_list1):
        raise AssertionError('The image must be in "compressed PGM format"...')
    return pixel_list1

def load_image(file_name):
    '''
    (str) --> (list<list>)
    This function takes as input a filename, and checks the first line of the
    file. If it is 'P2', it loads in the file as a regular PGM image and returns
    the image matrix. However if the first line is 'P2C', then loads in the file
    as a compressed PGM image and returns thr image matrix. If it is anything else,
    then an exception error is raised.
    
    >>> load_image('comp.pgm')
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    >>> load_image('comp.pgm.compressed')
    [['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]
    
    >>> fobj = open('invalid_test5.1.pgm','w')
    >>> fobj.write('P2C\\n a b c d e')
    14
    >>> fobj.close()
    >>> load_image('invalid_test5.1.pgm')
    Traceback (most recent call last):
    AssertionError: The image must be in "compressed PGM format"...
    '''
    fobj = open(file_name, 'r')
    for line in fobj:
        line_array = line.strip().split()
        break
    fobj.close()
    
    if line_array == ["P2"]:
        return load_regular_image(file_name)
    elif line_array == ["P2C"]:
        return load_compressed_image(file_name)
    else:
        raise AssertionError('The first line of file must either be P2 or P2C')

def save_regular_image(my_list, file_name):
    '''
    (list<list<str>>,str) --> (NoneType)
    
    This function saves the matrix int the PGM format to a file with the given filename.
    If the image matrix given as input is not a valid PGM image matrix,
    an AssertionError is raised  with an appropriate error message.
    
    >>> save_regular_image([[0]*10, [255]*10, [0]*10], "test.pgm")
    >>> fobj = open("test.pgm", 'r')
    >>> fobj.read()
    'P2\\n10 3\\n255\\n0 0 0 0 0 0 0 0 0 0\\n255 255 255 255 255 255 255 255 255 255\\n0 0 0 0 0 0 0 0 0 0\\n'
    >>> fobj.close()
    
    >>> save_regular_image([[1,2,3000],[2,2,255],[9,9,9]], 'invalid_test6.1.pgm')
    Traceback (most recent call last):
    AssertionError: The image must be in valid "PGM format"...
    
    >>> save_regular_image([[1,2,3,122],[3,4,5],[7,8,9]], 'invalid_test6.2.pgm')
    Traceback (most recent call last):
    AssertionError: The image must be in valid "PGM format"...
    '''
    if not is_valid_image(my_list):
        raise AssertionError ('The image must be in valid "PGM format"...')
    if type(file_name)!=str:
        raise AssertionError('The filename must be a string...')
    fobj = open(file_name,"w")
    height = len(my_list)
    width = len(my_list[0])
    string = ''
    for i in range(0,len(my_list)):
        for j in range(0,len(my_list[i])):
            string+= str(my_list[i][j])
            if j != len(my_list[i])-1:
                string += ' '
        string +='\n'

    fobj.write('P2\n'+str(width)+' '+str(height)+'\n'+'255'+'\n'+string)
    fobj.close()
    
def save_compressed_image(my_list,file_name):
    '''
    (list<list<str>>,str) --> (NoneType)
    
    This function takes a nested list and a filename as input and saves
    it in the compressed PGM format to a file with the given name. If the
    image matrix given as input is not a valid compresses PGM image matrix,
    then an Assertion Error is raised instead, with an appropriate error
    message.
    
    >>> save_compressed_image([['0x5','200x2'],['111x7']],'valid_test7.1.pgm')
    >>> fobj = open('valid_test7.1.pgm')
    >>> fobj.read()
    'P2C\\n7 2\\n255\\n0x5 200x2\\n111x7\\n'
    >>> fobj.close()
    
    >>> save_compressed_image([['10x20','5x20','15x10'],['40x25','40x25']],'valid_test7.2.pgm')
    >>> fobj = open('valid_test7.1.pgm')
    >>> fobj.read()
    'P2C\\n7 2\\n255\\n0x5 200x2\\n111x7\\n'
    >>> fobj.close()
    
    >>> save_compressed_image([['10x90','10x100'],['20x25','75x100']],'invalid_test7.1.pgm')
    Traceback (most recent call last):
    AssertionError: The image must be in valid "compressed PGM format"...
    '''
    if not is_valid_compressed_image(my_list):
        raise AssertionError ('The image must be in valid "compressed PGM format"...')
    if type(file_name)!=str:
        raise AssertionError('The filename must be a string...')
    fobj = open(file_name,"w")
    height = len(my_list)
    width = 0
    for j in range(0,len(my_list[0])):
        element=my_list[0][j]
        x_index = element.find('x') 
        B = element[x_index+1:]
        width += int(B)
    
    string = ''
    for row in range(0,height):
        for column in range(0,len(my_list[row])):
            if column != len(my_list[row])-1:
                string += my_list[row][column] + ' '
            else:
                string += my_list[row][column]
        string += '\n'

    fobj.write('P2C'+'\n'+str(width)+' '+str(height)+'\n'+'255'+'\n'+string)
    fobj.close()

    
def save_image(my_list,file_name):
    '''
    (list<list<str>>,str) --> (NoneType)
    
    This function checks the type of elements in the list. 
    If they are integers, then saves the nested list as PGM image
    matrix into a file with the given filename; if they are
    strings, then the function saves the nested list as a 
    compresses PGM image matrix into a the file of the
    given filename in argument. 
    Otherwise, it raises an Assertion Error.

    >>> save_image([["0x5", "200x2"], ["111x7"]], "valid_test8.1.pgm.compressed")
    >>> fobj = open("valid_test8.1.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\\n7 2\\n255\\n0x5 200x2\\n111x7\\n'
    >>> fobj.close()

    >>> save_image([[0,1,2,3],[4,5,6,7],[8,9,10,100]],"valid_test8.2.pgm")
    >>> fobj = open("valid_test8.2.pgm")
    >>> fobj.read()
    'P2\\n4 3\\n255\\n0 1 2 3\\n4 5 6 7\\n8 9 10 100\\n'
    >>> fobj.close()
    
    >>> save_image([[0,1,2,3,4],['1',2,3,4],[200]],"invalid_test8.1.pgm")
    Traceback (most recent call last):
    AssertionError: The nested list must be in "PGM format" or "compressed PGM format"...
    '''
    if type(file_name)!=str:
        raise AssertionError('The filename should be a string')
    if is_valid_image(my_list):
        save_regular_image(my_list,file_name)
    elif is_valid_compressed_image(my_list):
        save_compressed_image(my_list,file_name)
    else:
        raise AssertionError('The nested list must be in "PGM format" or "compressed PGM format"...')

def invert(my_list):
    '''
    (list<list<str>>) --> (list<list<str>>)
    
    This function returns the input image matrix inverted,
    and the input is not modified. An Assertion Error
    is raised if the PGM image matrix is not valid.

    >>> invert([[0, 100, 150], [200, 200, 200], [255, 255, 255]])
    [[255, 155, 105], [55, 55, 55], [0, 0, 0]]

    >>> invert([[0,100,150,200],[200,100,100,100],[50,50,50,50]])
    [[255, 155, 105, 55], [55, 155, 155, 155], [205, 205, 205, 205]]

    >>> invert([[300,100,150,200],[200,100,100,100],[50,50,50,50]])
    Traceback (most recent call last):
    AssertionError: The image must be in "PGM format"...
    '''
    if not is_valid_image(my_list):
        raise AssertionError('The image must be in "PGM format"...')

    new_list1= []
    for i in range(0,len(my_list)):
        new_list2=[]
        for j in range(0,len(my_list[i])):
            new_list2.append(255 - my_list[i][j])
        new_list1.append(new_list2)
    return new_list1

def flip_horizontal(my_list):
    '''
    (list<list<str>>) --> (list<list<str>>)

    This function returns the image matrix flipped horizontally.
    The input matrix should not be modified. If the input matrix
    is not a valid PGM image matrix, then an Assertion Error is
    raised.

    >>> flip_horizontal([[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]])
    [[5, 4, 3, 2, 1], [10, 10, 5, 0, 0], [5, 5, 5, 5, 5]]

    >>> flip_horizontal([[1,3,5,7,100],[10,10,20,20,30]])
    [[100, 7, 5, 3, 1], [30, 20, 20, 10, 10]]
    
    >>> flip_horizontal([[1,3,5,7,100],[10,10,20]])
    Traceback (most recent call last):
    AssertionError: The image must be in "PGM format"...
    '''
    if not is_valid_image(my_list):
        raise AssertionError('The image must be in "PGM format"...')
    
    new_list1=[]
    for i in range(0,len(my_list)):
        new_list2 = []
        for j in range(len(my_list[i])-1,-1,-1):
            new_list2.append(my_list[i][j])
        new_list1.append(new_list2)
    return new_list1

def flip_vertical(my_list):
    '''
    (list<list<str>>) --> (list<list<str>>)

    This function returns the image matrix flipped vertically.
    The input matrix should not be modified. If the input matrix
    is not a valid PGM image matrix, then an Assertion Error is
    raised.

    >>> image = [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    >>> flip_vertical(image)
    [[5, 5, 5, 5, 5], [0, 0, 5, 10, 10], [1, 2, 3, 4, 5]]
    
    >>> image = [[10,10,10,10],[10,20,20,40],[100,100,100,100]]
    >>> flip_vertical(image)
    [[100, 100, 100, 100], [10, 20, 20, 40], [10, 10, 10, 10]]
    >>> image
    [[10, 10, 10, 10], [10, 20, 20, 40], [100, 100, 100, 100]]
    
    >>> flip_vertical([[1,3,5,7,100],[10,10,20]])
    Traceback (most recent call last):
    AssertionError: The image must be in "PGM format"...
    '''
    if not is_valid_image(my_list):
        raise AssertionError('The image must be in "PGM format"...')
    new_list1 = []
    for i in range(len(my_list)-1,-1,-1):
        new_list1.append(my_list[i][:])
    return new_list1

def crop(my_list,num1,num2,num3,num4):
    '''
    (list<list<str>>,int,int,int,int) --> (list<list<str>>)
    
    The first two non-negative integers in the parameters passed correspond to
    the top left row and top left column of the target rectangle, and the two
    positive integers correspond to the number of rows and number of columns
    of the target rectangle. The function returns an image matrix corresponding
    to the pixels contained in the target rectangle. The input list is
    not modified.
    
    If the image_matrix is not a valid PGM matrix, an Assertion Error is
    raised.

    >>> crop([[5, 5, 5], [5, 6, 6], [6, 6, 7]], 1, 1, 2, 2)
    [[6, 6], [6, 7]]

    >>> crop([[5, 5, 5, 5, 8, 8], [5, 6, 6, 7, 9, 10], [6, 6, 7, 11, 12, 9], [4, 3, 6, 1, 9, 0]], 1, 2, 3, 3)
    [[6, 7, 9], [7, 11, 12], [6, 1, 9]]
    
    >>> crop([[4, 4, 4], ['2', 2, 3], [5, 6, 1]], 1, 1, 2, 2)
    Traceback (most recent call last):
    AssertionError: The image must be in "PGM format"...
    '''
    if not is_valid_image(my_list):
        raise AssertionError('The image must be in "PGM format"...')
    new_list=[]
    for i in range(num1,num3+num1):
        inner_list=[]
        for j in range(num2,num4+num2):
            inner_list.append(my_list[i][j])
        new_list.append(inner_list)
    
    return new_list

def find_end_of_repetition(my_list,index,target_num):
    '''
    (list<str>,int,int) --> int
    This function looks through the list of integers starting after the
    given index and returns the index of the last consecutive occurrence
    of the target number
    
    >>> find_end_of_repetition([5,3,5,5,5,-1,0],2,5)
    4

    >>> find_end_of_repetition([1,2,3,4,6,6,6],5,6)
    6

    >>> find_end_of_repetition([0,0,0,0,0,0],0,0)
    5
    '''

    for i in range(index,len(my_list)):
        if not(my_list[i]==target_num):
            return i-1
    if i == len(my_list)-1:
        return i

def compress(my_list):
    '''
    (list<list<str>>) --> (list<list<str>>)
    
    This function compresses the image matrix and returns the compressed image matrix.
    If the image matrix is not a valid format, an AsseetionError is raised.

    >>> compress([[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]])
    [['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']]

    >>> compress([[10, 10, 20, 25], [10, 15, 6, 6], [200, 200, 200, 200]])
    [['10x2', '20x1', '25x1'], ['10x1', '15x1', '6x2'], ['200x4']]

    >>> compress([['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']])
    Traceback (most recent call last):
    AssertionError: The image must be in valid "PGM format"...
    '''
    if not is_valid_image(my_list):
        raise AssertionError('The image must be in valid "PGM format"...')
    outer_list = []
    for i in range(0,len(my_list)):
        inner_list=[]
        j=0
        while j<len(my_list[i]):
            count = find_end_of_repetition(my_list[i],j,my_list[i][j])
            inner_list.append(str(my_list[i][j])+'x'+str(count+1-j))
            j=count+1
        outer_list.append(inner_list)
    return outer_list

def decompress(my_list):
    '''
    (list<list<str>>) --> (list<list<int>>)
    
    This function decompresses the image matrix that is input to it.
    If the input matrix is not a valid input matrix, then an AssertionError
    with a proper message is raised instead.
    
    >>> decompress([['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']])
    [[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]]
    
    >>> decompress([['11x7','4x2'], ['1x4', '5x2', '7x3'], ['255x3', '9x5', '255x1']])
    [[11, 11, 11, 11, 11, 11, 11, 4, 4], [1, 1, 1, 1, 5, 5, 7, 7, 7], [255, 255, 255, 9, 9, 9, 9, 9, 255]]
    
    >>> decompress([['11x9','10x0'], ['1x4', '5x2', '7x3'], ['255x3', '9x5', '255x1']])
    Traceback (most recent call last):
    AssertionError: The image is not in valid "compressed PGM format"...
    '''
    if not is_valid_compressed_image(my_list):
        raise AssertionError('The image is not in valid "compressed PGM format"...')
    new_outer_list=[]
    for i in range(0,len(my_list)):
        new_inner_list = []
        for j in range(0,len(my_list[i])):
            element = my_list[i][j]
            x_index = element.find('x')
            A = int(element[0:x_index])
            B = int(element[x_index+1:])
            for k in range(0,B):
                new_inner_list.append(A)
        new_outer_list.append(new_inner_list)
    return new_outer_list

def process_command(image_commands):
    '''
    (str) --> (NoneType)
    
    A command string can contain any of the following commands, which each correspond to one of
    the above functions: 'LOAD', 'SAVE', 'INV', 'FH', 'FV', 'CR', 'CP', 'DC'.

    >>> process_command("LOAD<comp.pgm> CP DC INV INV SAVE<comp2.test.pgm>")
    >>> image = load_image("comp.pgm")
    >>> image2 = load_image("comp2.test.pgm")
    >>> image == image2
    True

    >>> process_command("LOAD<comp.pgm> A SAVE<comp2.test.pgm>")
    Traceback (most recent call last):
    AssertionError: Unrecognized command A
    
    >>> process_command("LOAD<comp.pgm> CRB<1,2,3,4> SAVE<comp2.test.pgm>")
    Traceback (most recent call last):
    AssertionError: Unrecognized command CRB<1,2,3,4>
    '''
    commands_array = image_commands.split()

    load_command = commands_array[0]
    load_file_name = load_command[5:-1]
    image_matrix = load_image(load_file_name)

    for char in commands_array[1:-1]:
        if char == 'INV':
            image_matrix = invert(image_matrix)
        elif char == 'FH':
            image_matrix = flip_horizontal(image_matrix)
        elif char == 'FV':
            image_matrix = flip_vertical(image_matrix)
        elif char[0:3]=='CR<' and len(char)>=11:
            crop_array = char[3:-1].split(',')
            image_matrix = crop(image_matrix,int(crop_array[0]),int(crop_array[1]),int(crop_array[2]),int(crop_array[3]))
        elif char == 'CP':
            image_matrix = compress(image_matrix)
        elif char == 'DC':
            image_matrix = decompress(image_matrix)
        else:
            raise AssertionError('Unrecognized command ' + str(char))

    save_command = commands_array[-1]
    save_file_name = save_command[5:-1]
    save_image(image_matrix,save_file_name)


if __name__ == '__main__':
    doctest.testmod()
print('?'.isdigit())