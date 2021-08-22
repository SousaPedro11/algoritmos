package br.ufpa;

import java.time.LocalDate;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        Estado para = new Estado("Pará", "PA");
        Cidade belem = new Cidade("Belém", para);
        Endereco endereco1 = new Endereco(
                "Av. Perimetral",
                100,
                "Terra Firme",
                "66095-780",
                belem
        );
        Endereco endereco2 = new Endereco(
                "R. Augusto Corrêa",
                767,
                "Guamá",
                "66073-044",
                belem
        );
        Endereco endereco3 = new Endereco(
                "Pass. Sururina",
                237,
                "Guamá",
                "66075-440",
                belem
        );
        EquipeVenda equipeVenda = new EquipeVenda("White Tiger");
        Vendedor vendedor = new Vendedor(
                "Sérgio",
                LocalDate.of(1992, 10, 16),
                "150.000.000-00",
                1500.0,
                Arrays.asList(endereco1),
                equipeVenda
        );

        Gerente gerente = new Gerente(
                "Augustus",
                LocalDate.of(1985, 7, 17),
                "527.000.000-00",
                3000.0,
                Arrays.asList(endereco1, endereco2)
        );
        System.out.println(vendedor);
        System.out.println(gerente);
    }
}
