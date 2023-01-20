import sys
sys.path.append('../pypi-wrangler')
import my_build

def main():
    """
    For right now we're just testing the main functionality to build the "dist" directory.
    """
    
    my_build.dist('./requests_packages', './packages', True)


if __name__ == '__main__':
    main()