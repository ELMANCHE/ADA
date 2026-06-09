import java.util.Arrays;
import java.util.Comparator;

public class ejercio1 {

    // esta clase es para representar cada objeto
    static class Objeto {
        String nombre;
        double valor;
        double peso;
        double ratio;

        public Objeto(String nombre, double valor, double peso) {
            this.nombre = nombre;
            this.valor = valor;
            this.peso = peso;
            this.ratio = valor / peso; // Valor por unidad de peso es relevante 
        }
    }

    public static void resolverMochila(Objeto[] objetos, double capacidad) {
        // comenzamos por ordenar los objetos de mayor a menor usando comparator como se ve ahi
        Arrays.sort(objetos, new Comparator<Objeto>() {
            @Override
            public int compare(Objeto o1, Objeto o2) {
                return Double.compare(o2.ratio, o1.ratio);
            }
        });

        double capacidadRestante = capacidad;
        double valorTotal = 0.0;

        System.out.println("Objetos seleccionados:");

        // luego se debe recorrer los objetos ordenados
        for (Objeto obj : objetos) {
            if (capacidadRestante == 0) break;

            if (obj.peso <= capacidadRestante) {
                // el objeto se anade completamente
                capacidadRestante -= obj.peso;
                valorTotal += obj.valor;
                System.out.println(obj.nombre + " completo");
            } else {
                // el objeto se anade de forma fraccionada
                double fraccion = capacidadRestante / obj.peso;
                valorTotal += obj.valor * fraccion;
                
                // se obtiene una salida en forma de fraccion 
                System.out.println((int)capacidadRestante + "/" + (int)obj.peso + " Parte del objeto " + obj.nombre);
                capacidadRestante = 0; // aca se supone que la mochila esta llena 
            }
        }

        System.out.println("Valor total aproximado: " + valorTotal);
    }

    public static void main(String[] args) {
        // prueba1
        System.out.println("prueba1");
        Objeto[] objetos1 = {
            new Objeto("A", 60, 10),
            new Objeto("B", 100, 20),
            new Objeto("C", 120, 30)
        };
        resolverMochila(objetos1, 50);

        // prueba2
        System.out.println("\nprueba2");
        Objeto[] objetos2 = {
            new Objeto("A", 80, 20),
            new Objeto("B", 100, 10),
            new Objeto("C", 120, 30)
        };
        resolverMochila(objetos2, 25);
    }
}