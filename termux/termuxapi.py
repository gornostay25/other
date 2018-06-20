proc = subprocess.Popen(["termux-dialog -t test"], stdout=subprocess.PIPE, shell=True) \n a = proc.stdout \n a = a.read().strip().decode()
