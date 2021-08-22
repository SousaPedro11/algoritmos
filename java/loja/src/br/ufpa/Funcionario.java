package br.ufpa;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.List;
import java.util.stream.Collectors;

public class Funcionario {
    private final String nome;
    private final LocalDate nascimento;
    private final String cpf;
    private final Double salario;
    private final List<Endereco> enderecos;

    public Funcionario(String nome, LocalDate nascimento, String cpf, Double salario, List<Endereco> enderecos) {
        this.nome = nome;
        this.nascimento = nascimento;
        this.cpf = cpf;
        this.salario = salario;
        this.enderecos = enderecos;
    }

    public String getNome() {
        return nome;
    }

    public LocalDate getNascimento() {
        return nascimento;
    }

    public String getCpf() {
        return cpf;
    }

    public Double getSalario() {
        return salario;
    }

    public List<Endereco> getEnderecos() {
        return enderecos;
    }

    @Override
    public String toString() {
        DateTimeFormatter formatadorBarra = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        return "Cargo: " + this.getClass().getSimpleName() + "\n" +
                "Nome: " + this.getNome() + "\n" +
                "Nascimento: " + this.getNascimento().format(formatadorBarra) + "\n" +
                "CPF: " + this.getCpf() + "\n" +
                "Salario Base: " + this.salario + "\n" +
                "Salario: " + this.getSalario() + "\n" +
                "Enderecos: \n\t" + this.getEnderecos().stream()
                .map(Endereco::toString)
                .collect(Collectors.joining("\n\t")) + "\n";
    }
}
