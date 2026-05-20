"""
Seed extendido para poblar más registros y cumplir la cantidad mínima.
Ejecutar con: python manage.py shell < database/seed_extended.py
"""
import os, django, random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sigim.settings')
django.setup()

from django.contrib.auth.models import User
from inventario.models import Proveedor, Producto, MovimientoInventario, OrdenCompra

# Asegurar proveedores
if Proveedor.objects.count() < 6:
    for i in range(6):
        Proveedor.objects.get_or_create(nombre=f'Proveedor Ext {i+1}', defaults={'contacto':f'Contacto {i+1}','telefono':f'300000{i+1}','email':f'p{i+1}@prov.com','direccion':'Ciudad'})

proveedores = list(Proveedor.objects.all())

# Crear productos hasta 40
existing = Producto.objects.count()
target = 40
created = 0
categorias = ['Alimentos','Bebidas','Aseo','Lacteos','Hogar']
for i in range(existing+1, target+1):
    code = f'EXT-{i:03d}'
    nombre = f'Producto Ext {i}'
    prov = random.choice(proveedores)
    precio = random.randint(1000,20000)
    disp = random.randint(0,300)
    stock_min = random.randint(5,50)
    Producto.objects.get_or_create(codigo_unico=code, defaults=dict(nombre=nombre,categoria=random.choice(categorias),precio=precio,cantidad_disponible=disp,stock_minimo=stock_min,unidad_medida='UND',proveedor=prov))
    created += 1

print(f'✔ Productos añadidos: {created} (total ahora: {Producto.objects.count()})')

# Crear movimientos
users = list(User.objects.all())
productos = list(Producto.objects.all())
mov_created = 0
for i in range(60):
    producto = random.choice(productos)
    tipo = random.choice(['ENTRADA','SALIDA'])
    cantidad = random.randint(1,50)
    usuario = random.choice(users) if users else None
    MovimientoInventario.objects.create(tipo=tipo, cantidad=cantidad, descripcion='Seed automático', usuario_responsable=usuario, producto=producto)
    mov_created += 1

print(f'✔ Movimientos creados: {mov_created}')

# Crear órdenes de compra
oc_created = 0
for i in range(40):
    producto = random.choice(productos)
    proveedor = producto.proveedor or random.choice(proveedores)
    usuario = random.choice(users) if users else None
    cantidad = random.randint(5,100)
    OrdenCompra.objects.create(producto=producto, proveedor=proveedor, usuario=usuario, estado='SUGERIDA', cantidad_sugerida=cantidad, observaciones='Seed automático')
    oc_created += 1

print(f'✔ Órdenes creadas: {oc_created}')
print('\n✅ Seed extendido ejecutado.')
