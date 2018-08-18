package com.locadora.veiculos.model;

import java.time.LocalDateTime;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;
import javax.validation.constraints.NotNull;

@Entity
@Table(name = "checkout")
public class Checkout {

	@Column(name = "id_checkout")
	@Id
	@GeneratedValue
	private Long idCheckout;
	
	@NotNull
	@Column(name = "horario_co")
	private LocalDateTime horarioCheckOut;
	
	@ManyToOne
	@JoinColumn(name="cliente", nullable=false)
	//@ForeignKey(name="cliente_fk")
	private Cliente checkout = new Cliente();

	public Long getIdCheckout() {
		return idCheckout;
	}

	public void setIdCheckout(Long idCheckout) {
		this.idCheckout = idCheckout;
	}

	public LocalDateTime getHorarioCheckOut() {
		return horarioCheckOut;
	}

	public void setHorarioCheckOut(LocalDateTime horarioCheckOut) {
		this.horarioCheckOut = horarioCheckOut;
	}

	public Cliente getCheckout() {
		return checkout;
	}

	public void setCheckout(Cliente checkout) {
		this.checkout = checkout;
	}
	
}
