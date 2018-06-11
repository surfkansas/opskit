import argparse
import importlib
import os
import sys

def build_arg_parser():
    
    arg_parser = argparse.ArgumentParser(add_help=False)
    arg_parser.add_argument('product', nargs='?', default=None)
    arg_parser.add_argument('action', nargs='?', default=None)
    arg_parser.add_argument('--help', action='store_true')
    
    return arg_parser

def show_help(args, arg_parser):
    if args.product is None:
        module_name = 'opskit'
    else:
        module_name = 'opskit.{0}'.format(args.product.replace('-', '_'))

    try:
        module_instance = importlib.import_module(module_name)
        module_path = module_instance.__path__[0]
        help_name = 'help.txt'
        if args.action is not None:
            help_name = 'help_{0}.txt'.format(args.action)

        help_path = os.path.join(module_path, help_name)
        with open(help_path, 'r') as help_file:
            print()
            print(help_file.read())
            print()
    except:
        if args.action is not None:
            print('Unable to show help for module: {0}, action: {1}'.format(module_name, args.action))
        else:
            print('Unable to show help for module: {0}'.format(module_name))
        print()

def run_action(args):
    module_name = 'opskit.{0}'.format(args.product.replace('-', '_'))

    module_instance = importlib.import_module(module_name)
    class_instance = getattr(module_instance, args.action)
    action_instance = class_instance()

    action_instance.initialize(build_arg_parser())
    action_instance.run_action()

def main():

    arg_parser = build_arg_parser()

    args, unknown = arg_parser.parse_known_args()

    if args.help or args.product is None or args.action is None:
        show_help(args, arg_parser)
    else:
        run_action(args)

if __name__ == '__main__':
    main()