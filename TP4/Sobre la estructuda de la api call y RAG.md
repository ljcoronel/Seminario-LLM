Estuve repasando como los distintos modelos sugieren pasar la info recuperada para hacer RAG y es bastante varieble. Por lo pronto, muchos no tienen el historial aparte de la conversacion en un campo aparte, si no que tienen una estructura donde simplemente se alternan los mensajes indicando el rol. como el siguiente.

# --- CONSTRUCCIÓN DEL HISTORIAL ---
```
historial_con_rag = [
    # 1. Instrucciones base del sistema (System Prompt)
    {
        "role": "system",
        "content": "Eres Alex, el asistente virtual de FlyAmérica. Responde de forma amable y usa SIEMPRE la información del contexto provisto si el usuario hace preguntas específicas sobre políticas."
    },
   
    # TURNO 1: El usuario inicia el chat
    {
        "role": "user",
        "content": "Hola, tengo un vuelo reservado para el próximo mes y quería hacer un cambio."
    },
    {
        "role": "assistant",
        "content": "¡Hola! Claro que sí, te puedo ayudar con eso. ¿Me indicas tu código de reserva, por favor?"
    },
   
    # TURNO 2: El usuario da los datos pero cambia de tema
    {
        "role": "user",
        "content": "Es ABC123. Pero antes de cambiarlo, me surgió una duda. ¿Puedo llevar a mi gato conmigo en el avión? Es un viaje de Buenos Aires a Mendoza."
    },
    {
        "role": "assistant",
        "content": "¡Qué bueno que preguntes! Sí, permitimos mascotas en vuelos nacionales, pero aplicamos ciertas restricciones de peso y tamaño de transportín."
    },
   
    # TURNO 3 (Presente): El usuario pide el detalle específico
    {
        "role": "user",
        "content": "Perfecto, ¿cuáles son esos límites exactos y cuánto cuesta?"
    },
]
```

En ejemplo de arriba, el LLM toma el último mensaje del user como el que tiene que responder. el rol assistant es lo que respondió el modelo. Esta es la modalidad de openAI, que fue copiada por varios modelos. En el caso de openAI, la info de RAG se agrega así, pero el rol con que se agrega puede variar de modelo en modelo (busquen el caso del modelo que estén usando uds).
  
# --- INYECCIÓN DE RAG ---
```
    # Colocamos la información recuperada justo al final del historial para que el modelo la tenga fresca.
    # Usamos el rol 'system' o un mensaje formateado para darle el contexto.
    {
        "role": "system",
        "content": f"Información de soporte recuperada para responder la última pregunta:\n{documento_recuperado_rag}"
    }
```