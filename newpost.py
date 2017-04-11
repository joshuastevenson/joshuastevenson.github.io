from ruamel import yaml #pip install ruamel.yaml
from sys import argv, exit 
from os import path
import datetime

def help():
    print 'useage: "filename" "title" '

def main():
    print "hello"

    argc = len(argv)

    if argc == 1:
        help()
        exit()

    filename = argv[1]
    title = argv[2]

    if path.isfile(filename):
        print filename + "already exists"
        exit()
    

    tocname = "_data/toc.yml"
    with open(tocname, 'r') as f:
        fc = f.read()


    data = yaml.load(fc, yaml.RoundTripLoader)

    nc = {"title":title, "url":filename}


    data["pages"].append(nc)

    out = yaml.dump(data, Dumper=yaml.RoundTripDumper)
    with open(tocname, 'w') as f:
        f.write(out)
    # print out

    with open(filename, "w") as post:
        date = datetime.date.today().strftime("%Y-%m-%d")
        data = "".join(["---\n","title: ",title,"\nlastEdited: ",date ,"\n---\n# ", title])
        
        post.write(data)


if __name__ == "__main__":
    main()