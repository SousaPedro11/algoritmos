package br.ufpa;

public class Endereco {
    private final String rua;
    private final int numero;
    private final String bairro;
    private final String cep;
    private final Cidade cidade;

    public Endereco(String rua, int numero, String bairro, String cep, Cidade cidade) {
        this.rua = rua;
        this.numero = numero;
        this.bairro = bairro;
        this.cep = cep;
        this.cidade = cidade;
    }

    public String getRua() {
        return rua;
    }

    public int getNumero() {
        return numero;
    }

    public String getBairro() {
        return bairro;
    }

    public String getCep() {
        return cep;
    }

    public Cidade getCidade() {
        return cidade;
    }

    @Override
    public String toString() {
        return "Endereco{" +
                "rua='" + this.getRua() + '\'' +
                ", numero=" + this.getNumero() +
                ", bairro='" + this.getBairro() + '\'' +
                ", cep='" + this.getCep() + '\'' +
                ", cidade=" + this.getCidade().getNome() + "-" + this.getCidade().getEstado().getSigla() +
                '}';
    }
}
