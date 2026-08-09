def prime(p):
	num=p-1
	while(num>1):
		if p%num==0:
			return False
		else:
			num-=1
	return True

def alice(p,g):
	a=int(input("Decide your private key:"))
	A=(g**a)%p
	print("Alice' public key is", A)
	B=int(input("Enter Bob's Public Key:"))
	key=(B**a)%p
	print("key =", key)
	
def bob(p,g):
	b=int(input("Decide your private key:"))
	B=(g**b)%p
	print("Bob's public key is", B)
	A=int(input("Enter Alice' Public Key:"))
	key=(A**b)%p
	print("key =", key)
	
p=int(input("Enter a prime no.:"))
cond=prime(p)
if cond==False:
	print(p, "is not a prime no.")
	exit()
else:
	print("p =", p)
g=int(input("Enter generator value(less than p):"))
if g>=p:
	print(g, "should be less than", p)
	exit()
else:
	print("g =", g)
name=str(input("Are you alice or bob ?"))
name=name.lower()
if (name=="alice"):
	alice(p,g)
elif (name=="bob"):
	bob(p,g)
else:
	print("Invalid input")
	exit();
	

	
