import torch
import torch.nn as nn

def nn():
	inData = torch.randn(100)
	outData = model(inData)
	return jsonify(classes=outData.detach().numpy())

model = torch.nn.Linear(100, 20)
print(nn())