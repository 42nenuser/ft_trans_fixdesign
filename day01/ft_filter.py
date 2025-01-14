import sys

def ft_filter(function, iterable):
    return (item for item in iterable if function(item))


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        
        
        S = sys.argv[1]
        N = int(sys.argv[2])
        
        # no special character 
        assert S.isalnum() or all(c.isalnum() or c.isspace() for c in S), "the arguments are bad"
        
        words = S.split()
        result = [word for word in ft_filter(lambda w: len(w) > N, words)]
        
        print(result)
        
    except (ValueError, AssertionError) as e:
        print(e)

        
        
        
        