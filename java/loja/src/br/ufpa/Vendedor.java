package br.ufpa;

import java.time.LocalDate;
import java.util.List;

public class Vendedor extends Funcionario {
    private final EquipeVenda equipe;

    public Vendedor(String nome, LocalDate nascimento, String cpf, Double salario, List<Endereco> enderecos, EquipeVenda equipe) {
        super(nome, nascimento, cpf, salario, enderecos);
        this.equipe = equipe;
    }

    public EquipeVenda getEquipe() {
        return equipe;
    }

    public Double getBonificacao() {
        return super.getSalario() * 0.10;
    }

    @Override
    public Double getSalario() {
        return super.getSalario() + this.getBonificacao();
    }

    @Override
    public String toString() {
        return super.toString() +
                "Equipe de Venda: " + this.getEquipe().getNome() + "\n";
    }
}
