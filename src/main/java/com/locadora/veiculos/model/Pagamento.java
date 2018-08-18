package com.locadora.veiculos.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;
import javax.validation.constraints.NotNull;

@Entity
@Table(name = "pagamento")
public class Pagamento {
	
	@Column(name = "id_pagamento")
	@Id
	@GeneratedValue
	private Long idPagamento;
	
	@Column(name = "tipo_pagamento")
	@NotNull
	private String tipoPagemento;
	
	@Column(name = "nota_fiscal")
	@NotNull
	private Integer notaFiscal;
	
	@Column(name = "valor")
	@NotNull
	private Float valor;
	
	@Column(name = "numero_cartao")
	@NotNull
	private Integer numeroCartao;
	
	@ManyToOne
	@JoinColumn(name="cliente", nullable=false)
	//@ForeignKey(name="cliente_fk")
	private Cliente pagamento = new Cliente();

	public Long getIdPagamento() {
		return idPagamento;
	}

	public void setIdPagamento(Long idPagamento) {
		this.idPagamento = idPagamento;
	}

	public String getTipoPagemento() {
		return tipoPagemento;
	}

	public void setTipoPagemento(String tipoPagemento) {
		this.tipoPagemento = tipoPagemento;
	}

	public Integer getNotaFiscal() {
		return notaFiscal;
	}

	public void setNotaFiscal(Integer notaFiscal) {
		this.notaFiscal = notaFiscal;
	}

	public Float getValor() {
		return valor;
	}

	public void setValor(Float valor) {
		this.valor = valor;
	}

	public Integer getNumeroCartao() {
		return numeroCartao;
	}

	public void setNumeroCartao(Integer numeroCartao) {
		this.numeroCartao = numeroCartao;
	}

	public Cliente getPagamento() {
		return pagamento;
	}

	public void setPagamento(Cliente pagamento) {
		this.pagamento = pagamento;
	}

}
