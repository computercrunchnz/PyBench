import time
import math
import random

runs = input("Minutes to run for: ")

runsa = 0

runb = time.time() + 60 * int(runs)

while time.time() < runb:
    calct = random.randint(0,5)
    calc1 = random.randint(0,999999999)
    calc2 = random.randint(0,999999999)
    if calct == 0:
        a = calc1 + calc2
        b = calc1 - calc2
    elif calct == 1:
        a = calc1 * calc2
        b = calc1 / calc2
    elif calct == 2:
        a = math.e
        b = math.e
    elif calct == 3:
        a = math.pi
        b = math.pi
    elif calct == 4:
        a = math.cos(calc1)
        b = math.cos(calc2)
    elif calct == 5:
        a = math.sin(calc1)
        b = math.sin(calc2)
    elif calct == 6:
        a = math.tan(calc1)
        b = math.tan(calc2)
    elif calct == 7:
        a = math.factorial(calc1)
        b = math.factorial(calc2)
    
    print(a,b)
    
    print("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce at vulputate enim, et pharetra est. Cras vitae rutrum lacus, sed iaculis tellus. Sed aliquet mi at magna euismod mattis. Sed in lorem pellentesque, blandit orci vel, scelerisque nunc. Donec a ex nibh. Maecenas a faucibus tellus, ac laoreet ligula. Ut ac ante ac ligula bibendum mollis nec viverra enim. Etiam luctus lorem purus, eget tincidunt leo sollicitudin eget. Vestibulum ac neque at arcu euismod maximus. Fusce eget pellentesque ante. Quisque vitae mauris rutrum, laoreet quam eu, iaculis nibh. Praesent lobortis mollis vestibulum. Sed imperdiet turpis vel augue fringilla vulputate. In est neque, sollicitudin id nunc nec, mollis luctus erat. Integer non congue nunc, vel consequat est. Aliquam faucibus aliquet dolor, et pharetra augue pellentesque molestie. Ut id feugiat magna. Integer quis erat erat. Maecenas elementum dolor quis nisi pulvinar, at dictum mauris auctor. Aliquam aliquam mauris nulla, ut viverra ex ultricies ut. Praesent auctor augue non nunc blandit condimentum. Vestibulum nec ipsum velit. Proin commodo pharetra libero non vestibulum. Cras porttitor lobortis mauris, sed euismod est pretium et. Ut imperdiet quam quis dolor vehicula tempus. Curabitur erat ante, convallis at lorem quis, hendrerit elementum nulla. Nullam faucibus aliquam maximus. Nam condimentum nibh vitae massa mattis, ac varius lacus semper. Proin tempor augue maximus tincidunt vestibulum. Integer consectetur tellus eu odio auctor elementum. Mauris tincidunt diam nec luctus porta. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum turpis justo, pulvinar ultricies efficitur vel, bibendum ac justo. Mauris lacinia porttitor libero, quis fermentum purus. Mauris odio tortor, egestas id odio eu, commodo finibus nibh. Suspendisse potenti. In venenatis purus sit amet ex finibus, sed consectetur eros vehicula. Donec ut maximus lacus, sit amet rhoncus justo. Fusce nec dui turpis. Cras sed efficitur ligula. Duis at ligula orci. Integer malesuada aliquet sem id consequat. Proin elit lacus, vulputate ac pharetra in, aliquam ac mi. Sed rhoncus erat ac nisl iaculis accumsan. Sed nunc lorem, finibus at eros condimentum, scelerisque eleifend metus.")
    
    runsa = runsa + 1
    
runs = runsa

print("Done!")
print("Score: " + str(runsa))
