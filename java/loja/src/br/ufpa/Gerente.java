package br.ufpa;

import java.time.LocalDate;
import java.util.Date;
import java.util.List;

public class Gerente extends Funcionario {
    public Gerente(String nome, LocalDate nascimento, String cpf, Double salario, List<Endereco> enderecos) {
        super(nome, nascimento, cpf, salario, enderecos);
    }

    public Double getBonificacao() {
        return super.getSalario() * 0.15;
    }

    @Override
    public Double getSalario() {
        return super.getSalario() + this.getBonificacao();
    }
}
