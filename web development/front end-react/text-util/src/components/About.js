import React from "react";

export default function About(props) {
   let mystyle = {
     color: props.mode === "dark" ? "white" : "black",
   };
  return (
    <>
      <div className="container" style={mystyle}>
        <h1 className="my-3 ">About us</h1>
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Temporibus,
        atque. Minus quaerat, eius modi laboriosam tempore natus incidunt harum
        quam. Quam consectetur libero perspiciatis pariatur similique maxime
        reprehenderit architecto quia voluptatibus at sed expedita ipsa modi
        omnis quos nisi aliquid tenetur veritatis, quis nam totam vero delectus
        in accusamus! Voluptatibus, nemo? Tempora laborum omnis modi dolor dicta
        autem neque in, molestias non magnam ex aliquid officia praesentium
        dolorum, quisquam doloremque consectetur rerum nostrum molestiae quos
        fugit at. Veritatis, possimus ut!
      </div>
    </>
  );
}
