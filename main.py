kanban = [[],[],[]]
k = {
    "afazer": [],
    "analise": [],
    "desenvolvimento": [],
    "teste": [],
    "finalizado": []
}
# k["afazer"].append("criar login")
# print(k["afazer"][0])
# mover = k["afazer"].pop(k["afazer"].index("criar login"))
# k["analise"].append(mover)
# print(k["afazer"])
# print(k["analise"])
k["afazer"] = [
    "criar login",
    "criar cadastro",
    "criar banco"
]
print("tarefa:")
for i,tarefa in enumerate(k["afazer"]):
    print(f"{i+1} - {tarefa}")
choice = int(input("qual deseja mover?"))-1
mover = k["afazer"].pop(choice)
k["analise"].append(mover)

print(k["afazer"])
print(k["analise"])
