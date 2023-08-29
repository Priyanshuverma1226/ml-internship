# l=["Name","F Name","DOB","Phone Number"]
# stu1=['Sample','sim','25 May 2003','8076007125']

stu1={'Name':'Sample',
      'F_Name':'Sim',
      "DOB":"25 May 2003",
      "Phone Number":"8076007125"}
print(stu1['Name'])
print(len(stu1))
print(type(stu1))
p=stu1['DOB']
print(p)
print(stu1.keys())
print(stu1.items())
print(stu1.values())
stu1['Name']="Priyanshu"
print(stu1)
stu1['email']='p.verma1226@gmail.com'
# stu1.update("")
stu1.pop('Name')
stu1.clear()
print(stu1)