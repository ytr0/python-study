import sys
import astor
import hashlib

for file in sys.argv[1:]:
    ast = astor.parse_file(file)
    dumped_ast = astor.dump_tree(ast)
    hashed_ast = hashlib.md5(dumped_ast.encode('utf-8')).hexdigest()
    print("{} {}".format(file, hashed_ast))

#https://tech-blog.monotaro.com/entry/2018/09/26/142451
#python3 ast_analyzer.py a.py b.py