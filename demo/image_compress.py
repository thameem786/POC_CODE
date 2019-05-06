
import os
import sys
from PIL import Image

img_pat = r"C:\\Users\\thameem.sakkarai\\Documents\\images"
def compressMeReturn(file, maxDim, verbose=False):
    filepath = os.path.join(img_pat, file)
    print('filepath',filepath)
    oldsize = os.stat(filepath).st_size
    picture = Image.open(filepath)
    dim = picture.size
    print(dim,oldsize)

    ratio = (maxDim/dim[0] , maxDim / dim[1])

    picture.thumbnail((dim[0] * ratio[0], dim[1] * ratio[1]), Image.ANTIALIAS)
    picture.save("Compressed_" + file, "JPEG", optimize=True, quality=65)
    new_picture = Image.open(os.path.join(os.getcwd(), "Compressed_" + file))
    dim = new_picture.size

    newsize = os.stat(os.path.join(os.getcwd(), "Compressed_" + file)).st_size
    print(dim,newsize)
    percent = (oldsize - newsize) / float(oldsize) * 100
    if (verbose):
        print("File compressed from {0} to {1} or {2}%".format(oldsize, newsize, percent))
    return percent


def main():
    maxDimension = 600
    verbose = True
    # if (len(sys.argv) > 2):
    #     if (sys.argv[2].lower() == "-v"):
    #         verbose = True


    tot = 0
    num = 0
    for file in os.listdir(img_pat):
        print(file)
        if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
            num += 1
            tot += compressMeReturn(file, int(maxDimension), verbose)
    print("Average Compression: %d" % (float(tot) / num))


if __name__ == "__main__":
    main()


