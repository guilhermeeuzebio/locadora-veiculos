package com.locadora.veiculos.model;

import java.util.ArrayList;
import java.util.List;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.JoinTable;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToMany;
import javax.persistence.Table;
import javax.validation.constraints.NotNull;

@Entity
@Table(name = "carro")
public class Carro {
	
	@Column(name = "id_carro")
	@Id
	@GeneratedValue
	private Long idCarro;
	
	@Column(name = "marca")
	@NotNull
	private String marca;
	
	@Column(name = "modelo")
	@NotNull
	private String modelo;
	
	@Column(name = "placa")
	@NotNull
	private String placa;
	
	@Column(name = "cor")
	@NotNull
	private String cor;
	
	@Column(name = "ano")
	@NotNull
	private Integer ano;

	@Column(name = "renavam")
	@NotNull
	private String renavam;
	
	@Column(name = "km_rodados")
	@NotNull
	private Integer kmRodados ;
	
	@Column(name = "tipo_combustivel")
	@NotNull
	private String tipoCombustivel;
	
	@Column(name = "qnt_assentos")
	@NotNull
	private Integer qntAssentos;
	
	@ManyToMany(cascade = CascadeType.ALL)
	@JoinTable(name = "carro_cliente", joinColumns = @JoinColumn(name = "id_carro"), inverseJoinColumns = @JoinColumn(name = "id_cliente"))
	private List<Cliente> cliente = new ArrayList<Cliente>();

	public Long getIdCarro() {
		return idCarro;
	}

	public void setIdCarro(Long idCarro) {
		this.idCarro = idCarro;
	}

	public String getMarca() {
		return marca;
	}

	public void setMarca(String marca) {
		this.marca = marca;
	}

	public String getModelo() {
		return modelo;
	}

	public void setModelo(String modelo) {
		this.modelo = modelo;
	}

	public String getPlaca() {
		return placa;
	}

	public void setPlaca(String placa) {
		this.placa = placa;
	}

	public String getCor() {
		return cor;
	}

	public void setCor(String cor) {
		this.cor = cor;
	}

	public Integer getAno() {
		return ano;
	}

	public void setAno(Integer ano) {
		this.ano = ano;
	}

	public String getRenavam() {
		return renavam;
	}

	public void setRenavam(String renavam) {
		this.renavam = renavam;
	}

	public Integer getKmRodados() {
		return kmRodados;
	}

	public void setKmRodados(Integer kmRodados) {
		this.kmRodados = kmRodados;
	}

	public String getTipoCombustivel() {
		return tipoCombustivel;
	}

	public void setTipoCombustivel(String tipoCombustivel) {
		this.tipoCombustivel = tipoCombustivel;
	}

	public Integer getQntAssentos() {
		return qntAssentos;
	}

	public void setQntAssentos(Integer qntAssentos) {
		this.qntAssentos = qntAssentos;
	}

	public List<Cliente> getCliente() {
		return cliente;
	}

	public void setCliente(List<Cliente> cliente) {
		this.cliente = cliente;
	}
	
}
