package com.locadora.veiculos.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.OneToOne;
import javax.persistence.Table;
import javax.validation.constraints.NotNull;

@Entity
@Table(name = "endereco")
public class Endereco {
	
	@Column(name = "id_endereco")
	@Id
	@GeneratedValue
	private Long idEndereco;
	
	@Column(name = "quadra")
	@NotNull
	private String quadra;

	@Column(name = "rua")
	@NotNull
	private String rua;
	
	@Column(name = "bairro")
	@NotNull
	private String bairro;
	
	@Column(name = "cep")
	@NotNull
	private Integer cep;
	
	@Column(name = "numero")
	@NotNull
	private Integer numero;
	
	@OneToOne(fetch = FetchType.EAGER)
	private Cliente cliente;

	public Long getIdEndereco() {
		return idEndereco;
	}

	public void setIdEndereco(Long idEndereco) {
		this.idEndereco = idEndereco;
	}

	public String getQuadra() {
		return quadra;
	}

	public void setQuadra(String quadra) {
		this.quadra = quadra;
	}

	public String getRua() {
		return rua;
	}

	public void setRua(String rua) {
		this.rua = rua;
	}

	public String getBairro() {
		return bairro;
	}

	public void setBairro(String bairro) {
		this.bairro = bairro;
	}

	public Integer getCep() {
		return cep;
	}

	public void setCep(Integer cep) {
		this.cep = cep;
	}

	public Integer getNumero() {
		return numero;
	}

	public void setNumero(Integer numero) {
		this.numero = numero;
	}

	public Cliente getCliente() {
		return cliente;
	}

	public void setCliente(Cliente cliente) {
		this.cliente = cliente;
	} 

}
