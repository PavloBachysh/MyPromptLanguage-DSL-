# MyPromptLanguage-DSL-
-Metaprogrammin assignment-

  All syntax is described in "grammar.tx"
  User should write prompt in "prompt.conf"
  After you write prompt run "compiler.py"
  (textX should be installed, if it's not than run "pip install textX")
  Output is saved in "output.json"

Prompt exsample:

  model = gpt-4o
  temperature = 0.6
  max_completion_tokens = 300
  frequency_penalty = 0.5
  reasoning_effort = low
  messages {
      {
          role:system,
          content : "You are a child"
      },
      (user): "What is your favourite animal?",
      (assistant) - "My favourite animal is cat",
      (user)"And why?"
  }

There are different ways to write messages:
  1 - 
      {
          role: role,
          content : "message"
      }
  2 - (role): "message"
  3 - (role) - "message"
  4 - (role)"message"

Some additional info:
  Not mentioned in exsample parametrs:
    top_p (not recomended to use with temperature)
    presence_penalty

  Limits:
    temperature [0.0; 2.0]
    top_p [0.0; 1.0]
    max_completion_tokens (0; +inf)
    presence_penalty [-2.0; 2.0]
    frequency_penalty [-2.0; 2.0]

    
  reasoning_effort can be low, medium and high
  model can be gpt-4o and gpt-4-turbo
