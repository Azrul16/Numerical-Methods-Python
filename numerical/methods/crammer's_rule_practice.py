import numpy as np # type: ignore

A=np.array([
    [10, -10, 0],
    [0, 10, -10],
    [0, 0, 10]
])

b=np.array([19.62, 29.43, 24.525])
det_A=np.linalg.det(A)

A_x=A.copy()
A_x[:,0]=b
det_x=np.linalg.det(A_x)

A_y=A.copy()
A_y[:,1]=b
det_y=np.linalg.det(A_y)

A_z=A.copy()
A_z[:,2]=b
det_z=np.linalg.det(A_z)

x = det_x / det_A
y = det_y / det_A
z = det_z / det_A

print(f"x={x}" )
print(f"y={y}" )
print(f"y={z}" )
