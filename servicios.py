from abc import ABC, abstractmethod

# 1. Clase Abstracta General que representa entidades del sistema
class EntidadBase(ABC):
    def __init__(self, id_entidad, nombre):
        self._id_entidad = id_entidad  # Encapsulamiento protegido
        self._nombre = nombre

    @abstractmethod
    def mostrar_detalles(self):
        """Método abstracto que obligatoriamente deben implementar las clases hijas"""
        pass

# 2. Clase Abstracta Servicio que hereda de EntidadBase
class Servicio(EntidadBase):
    def __init__(self, id_servicio, nombre, precio_base):
        super().__init__(id_servicio, nombre)
        self._precio_base = precio_base

    # Simulación de sobrecarga de métodos en Python usando valores por defecto
    def calcular_costo(self, descuento=0.0, impuesto=0.0):
        costo = self._precio_base - (self._precio_base * descuento)
        costo_final = costo + (costo * impuesto)
        return costo_final

    @abstractmethod
    def mostrar_detalles(self):
        pass

# 3. Primer servicio especializado: Reserva de Salas
class ReservaSala(Servicio):
    def __init__(self, id_servicio, nombre, precio_base, capacidad, tiene_proyector):
        super().__init__(id_servicio, nombre, precio_base)
        self._capacidad = capacidad
        self._tiene_proyector = tiene_proyector

    # Polimorfismo: Sobrescribiendo el método mostrar_detalles
    def mostrar_detalles(self):
        proyector = "Sí" if self._tiene_proyector else "No"
        return f"[Sala] {self._nombre} | Capacidad: {self._capacidad} pax | Proyector: {proyector} | Precio: ${self._precio_base}"

# 4. Segundo servicio especializado: Alquiler de Equipos
class AlquilerEquipo(Servicio):
    def __init__(self, id_servicio, nombre, precio_base, tipo_equipo, dias_alquiler):
        super().__init__(id_servicio, nombre, precio_base)
        self._tipo_equipo = tipo_equipo
        self._dias_alquiler = dias_alquiler

    # Polimorfismo y Sobrecarga: Se ajusta el cálculo de costo multiplicando por días
    def calcular_costo(self, descuento=0.0, impuesto=0.0):
        costo_total = self._precio_base * self._dias_alquiler
        costo = costo_total - (costo_total * descuento)
        return costo + (costo * impuesto)

    def mostrar_detalles(self):
        return f"[Equipo] {self._nombre} ({self._tipo_equipo}) | Tiempo: {self._dias_alquiler} días | Precio/día: ${self._precio_base}"

# 5. Tercer servicio especializado: Asesorías
class AsesoriaEspecializada(Servicio):
    def __init__(self, id_servicio, nombre, precio_base, area_experta, horas):
        super().__init__(id_servicio, nombre, precio_base)
        self._area_experta = area_experta
        self._horas = horas

    # Polimorfismo y Sobrecarga: Se ajusta el cálculo de costo multiplicando por horas
    def calcular_costo(self, descuento=0.0, impuesto=0.0):
        costo_total = self._precio_base * self._horas
        costo = costo_total - (costo_total * descuento)
        return costo + (costo * impuesto)

    def mostrar_detalles(self):
        return f"[Asesoría] {self._nombre} | Área: {self._area_experta} | Tiempo: {self._horas} horas | Tarifa/hora: ${self._precio_base}"



    # 5. Bloque de prueba con Manejo de Excepciones para garantizar robustez
if __name__ == "__main__":
    print("--- SISTEMA DE GESTIÓN DE SERVICIOS ---")
    try:
        # Validando entrada de datos numéricos para evitar errores de tipo
        precio_input = float(input("Ingrese el precio base del servicio: "))
        capacidad_input = int(input("Ingrese la capacidad de personas: "))
        
        # Instanciando una reserva de prueba
        sala_prueba = ReservaSala("S01", "Sala Principal", precio_input, capacidad_input, True)
        print("\n--- DETALLES DEL SERVICIO ---")
        print(sala_prueba.mostrar_detalles())
        print(f"Costo calculado: ${sala_prueba.calcular_costo(0.0, 0.19)}")
        
    except ValueError:
        print("\n[ERROR DE EXCEPCIÓN]: Debe ingresar valores numéricos válidos para el precio y la capacidad.")
    except Exception as e:
        print(f"\n[ERROR INESPERADO]: Ocurrió un fallo en el sistema: {e}")
        