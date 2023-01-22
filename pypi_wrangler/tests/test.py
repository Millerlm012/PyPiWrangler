import sys
sys.path.append('../pypi_wrangler')
import wrangle

def main():
    """
    For right now we're just testing the main functionality to build the "dist" directory.
    """
    
    wrangle.create_dist('./requests_packages', './packages', True)


if __name__ == '__main__':
    main()