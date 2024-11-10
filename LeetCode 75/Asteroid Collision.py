def asteroidCollision(asteroids):
    stack_ = []
    for asteroid in asteroids:
        curr_dir = "left" if asteroid < 0 else "right"
        curr_pow = abs(asteroid)

        while len(stack_) > 0 and curr_pow != None:
            prev_dir, prev_pow = stack_[-1]
            if prev_dir == "right" and curr_dir == "left":
                if prev_pow < curr_pow:
                    stack_.pop()
                elif prev_pow > curr_pow:
                    curr_pow = curr_dir = None
                else:
                    stack_.pop()
                    curr_pow = curr_dir = None
            else:
                break
        if curr_pow != None:
            stack_.append([curr_dir, curr_pow])
    return [-pow if dir == "left" else pow for dir, pow in stack_]

if __name__ == "__main__":
    asteroids = [5,10,-5]
    #asteroids = [-2,-2,1,-2]
    print("Result:",asteroidCollision(asteroids))
            
            
