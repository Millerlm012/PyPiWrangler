import sys
sys.path.append('../pypi-wrangler')
import wrangle

def main():
    """
    For right now we're just testing the main functionality to build the "dist" directory.
    """
    
    wrangle.dist('./requests_packages', './packages', True)


if __name__ == '__main__':
    main()