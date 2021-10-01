compute = input('\nYour expression? => ')
if not compute:
print ("No input")
else:
print ("Result =", eval(comp))


address = request.args.get("address")
cmd = "ping -c 1 %s" % address
subprocess.Popen(cmd, shell=True)
