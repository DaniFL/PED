use std::io;
use rand::Rng;

#[derive(Debug, PartialEq)]
enum Opcion {
    Piedra,
    Papel,
    Tijera,
}

impl Opcion {
    fn from_str(input: &str) -> Option<Opcion> {
        match input.trim().to_lowercase().as_str() {
            "piedra" => Some(Opcion::Piedra),
            "papel" => Some(Opcion::Papel),
            "tijera" => Some(Opcion::Tijera),
            _ => None,
        }
    }
}

fn obtener_opcion_computadora() -> Opcion {
    let mut rng = rand::thread_rng();
    match rng.gen_range(0..=2) {
        0 => Opcion::Piedra,
        1 => Opcion::Papel,
        _ => Opcion::Tijera,
    }
}

fn determinar_ganador(jugador: Opcion, computadora: Opcion) -> &'static str {
    match (jugador, computadora) {
        (Opcion::Piedra, Opcion::Tijera) |
        (Opcion::Papel, Opcion::Piedra) |
        (Opcion::Tijera, Opcion::Papel) => "¡Ganaste!",
        (Opcion::Piedra, Opcion::Papel) |
        (Opcion::Papel, Opcion::Tijera) |
        (Opcion::Tijera, Opcion::Piedra) => "¡Perdiste!",
        _ => "¡Empate!",
    }
}

fn main() {
    println!("Bienvenido al juego de Piedra, Papel o Tijera!");
    loop {
        println!("Elige tu opción (piedra, papel o tijera):");

        let mut entrada = String::new();
        io::stdin().read_line(&mut entrada).expect("Error al leer la entrada.");

        let opcion_jugador = match Opcion::from_str(&entrada) {
            Some(opcion) => opcion,
            None => {
                println!("¡Opción no válida! Por favor, elige entre piedra, papel o tijera.");
                continue;
            }
        };

        let opcion_computadora = obtener_opcion_computadora();

        println!("Tu elección: {:?}", opcion_jugador);
        println!("Elección de la computadora: {:?}", opcion_computadora);

        let resultado = determinar_ganador(opcion_jugador, opcion_computadora);
        println!("{}", resultado);

        println!("¿Quieres jugar de nuevo? (s/n)");

        let mut respuesta = String::new();
        io::stdin().read_line(&mut respuesta).expect("Error al leer la respuesta.");

    println!("¡Hola,!");
    println!("¡Hola,!");
    println!("¡Hola,!");
    println!("caracola,!");
    println!("¡Hola,!");
    println!("feo,!");
    println!("¡Hola,!");
    println!("¡HH");
}
