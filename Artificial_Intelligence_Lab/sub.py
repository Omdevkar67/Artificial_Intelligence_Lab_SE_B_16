print("select the subject \n math\n physics\n chemistry\n biology\n programming\n circuits\n statistics.\n AI Concepts")
sub1=input("choose the 1st subject:")
sub2=input("choose the 2nd subject:")
if(sub1=="math"and sub2=="physics")or(sub1=="physics"and sub2=="math"):
	print("Suggest brach is Mechanical Engineering")
elif(sub1=="math"and sub2=="programming")or(sub1=="programming"and sub2=="math"):
	print("Suggest brach is Computer Engineering")
elif(sub1=="statistics"and sub2=="programming")or(sub1=="programming"and sub2=="statistics"):
	print("Suggest brach is Artificial Intelligence and Data Science")
elif(sub1=="AI Concepts"and sub2=="programming")or(sub1=="programming"and sub2=="AI Concepts"):
	print("Suggest brach is Artificial Intelligence and Machine Learning Engineering")
elif(sub1=="math"and sub2=="circuits")or(sub1=="circuits"and sub2=="math"):
	print("Suggest brach is Electronics Engineering")
elif(sub1== "Biology"and sub2=="Chemistry")or(sub1=="Chemistry"and sub2== "Biology"):
	print("Suggest brach is Biotechnology")
