def trocar_valores(dicionario):
  temp = dicionario["K"]
  dicionario["K"] = dicionario["J"]
  dicionario["J"] = temp


dicionario_test = {"K":5,
                   "J":7}
print("O valor de K é %d e J é %d" % (dicionario_test["K"], \
                                       dicionario_test["J"]))
trocar_valores(dicionario_test)
print("O valor de K é %d e J é %d" % (dicionario_test["K"], \
                                       dicionario_test["J"]))
