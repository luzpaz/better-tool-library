#!/usr/bin/python3
import os
import sys
import argparse
from tooldb import ToolDB, Tool, Library, serializers
from tooldb.shape import get_shape_file_from_shape, get_properties_from_shape


def select_library(libraries):
    # No need to choose if there's just one.
    if len(libraries) == 1:
        return libraries[0]

    # Print the list of libraries including a number.
    libraries = list(enumerate(sorted(libraries, key=lambda l: l.label), start=1))
    default = None
    for n, lib in libraries:
        if lib.label == 'Default':
            default = n
        print('{}) {}{}'.format(n, lib.label, '*' if lib.label == 'Default' else ''))

    # Let the user choose.
    while True:
        try:
            selection = int(input('Please select the library number [{}]'.format(default)) or 1)
        except ValueError:
            continue
        return libraries[selection-1][1]

def create_tool(shape):
    shape_file = get_shape_file_from_shape(shape)

    # Reading the shape file requires the FreeCAD Python module to be installed.
    try:
        properties = get_properties_from_shape(shape_file)
    except ImportError:
        sys.stderr.write('error: FreeCAD Python module not found.' \
                       + ' Make sure it is installed and in your PYTHONPATH')
        sys.exit(1)

    # Ask for mandatory base parameters.
    label = input('Please enter a tool name (label): ')
    tool = Tool(label, shape)

    # Ask for tool-specific parameters as extracted from the shape file.
    print('Please enter the tool parameters (enter accepts default).')
    for group, propname, value, unit, enum in properties:
        enum_msg = 'Allowed values: ' + ', '.join(enum) if enum else ''
        msg = '{}/{} Unit is {}. {} [{}]: '.format(group, propname, unit, enum_msg, value)
        while True:
            val = input(msg) or value
            if enum and val not in enum:
                continue
            break
        tool.params[propname] = val

    return tool

parser = argparse.ArgumentParser(
    prog=__file__,
    description='CLI tool to manage a tool library'
)

# Common arguments
parser.add_argument('-f', '--format',
                    help='the type (format) of the library',
                    choices=sorted(serializers.serializers.keys()),
                    default='freecad')
parser.add_argument('name',
                    help='the DB name. In case of a file based DB, this is the path to the DB')
subparsers = parser.add_subparsers(dest='command', metavar='COMMAND')

# "ls" command arguments
lsparser = subparsers.add_parser('ls', help='list objects')
lsparser.add_argument('objects',
                      help='which DB object to work with',
                      nargs='*',
                      choices=['all', 'libraries', 'tools'])

# "export" command arguments
exportparser = subparsers.add_parser('export', help='export tools and libraries in a defined format')
exportparser.add_argument('-f', '--format',
                          dest='output_format',
                          help='target format',
                          choices=sorted(serializers.serializers.keys()),
                          required=True)
exportparser.add_argument('output',
                          help='the output DB name. In case of a file based DB, this is the path to the DB')

# "create" command arguments
createparser = subparsers.add_parser('create', help='create tools or libraries')
createsubparsers = createparser.add_subparsers(dest='object', metavar='OBJECT')

createtoolparser = createsubparsers.add_parser('tool', help='create a new tool')
createtoolparser.add_argument('shape', help='the type of tool. may be built-in shape, or a filename')

createlibraryparser = createsubparsers.add_parser('library', help='create a new library')


args = parser.parse_args()

serializer_cls = serializers.serializers[args.format]
serializer = serializer_cls(args.name)
db = ToolDB()
db.deserialize(serializer)

if args.command == 'ls':
    for obj in args.objects:
        if obj == 'libraries':
            for lib in db.libraries.values():
                print(lib)
        elif obj == 'tools':
            for tool in db.tools.values():
                print(tool)
        elif obj == 'all' or not obj:
            db.dump()
        else:
            parser.error('invalid object requested: {}'.format(args.object))

elif args.command == 'export':
    print("Exporting as {}".format(args.output_format))
    output_serializer_cls = serializers.serializers[args.output_format]
    output_serializer = output_serializer_cls(args.output)
    db.serialize(output_serializer)

elif args.command == 'create':
    if args.object == 'tool':
        library = select_library(list(db.get_libraries()))
        print('Tool will be added to library "{}".'.format(library.label))

        tool = create_tool(args.shape)
        db.add_tool(tool, library=library)
        library.serialize(serializer)
    elif args.object == 'library':
        tool = Library()
        parser.error('sorry, not yet implemented') #TODO
    else:
        parser.error('requested unsupported object: {}'.format(args.object))
    db.serialize(serializer)

else:
    print("no command given, nothing to do")
