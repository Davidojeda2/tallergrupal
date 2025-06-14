import temp_converciones

celsius = 20
fahrenheit = temp_converciones.C_to_F(celsius)
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit")

fahrenheit = 68
celsius = temp_converciones.F_to_C(fahrenheit)
print(f"{fahrenheit} grados Fahrenheit son {celsius} grados Celsius")

kelvin = 300
celsius = temp_converciones.K_to_C(kelvin)
print(f"{kelvin} grados Kelvin son {celsius} grados Celsius")

celsius = 25
kelvin = temp_converciones.C_to_K(celsius)
print(f"{celsius} grados Celsius son {kelvin} grados Kelvin")

fahrenheit = 32
kelvin = temp_converciones.F_to_K(fahrenheit)
print(f"{fahrenheit} grados Fahrenheit son {kelvin} grados Kelvin")

kelvin = 300
fahrenheit = temp_converciones.K_to_F(kelvin)
print(f"{kelvin} grados Kelvin son {fahrenheit} grados Fahrenheit")
