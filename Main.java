public class Main {

    public static void main(String[] args) {
        int[] datos = {5, 3, 8, 2};

        System.out.println("Bubble Sort:");
        OrdenamientoBase.bubbleSort(datos);
        OrdenamientoBase.imprimirArreglo(datos);

        int[] datos2 = {5, 3, 8, 2};
        System.out.println("Selection Sort:");
        OrdenamientoBase.selectionSort(datos2);
        OrdenamientoBase.imprimirArreglo(datos2);
    }
}
