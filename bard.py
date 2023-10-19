import requests
import certifi

response = requests.get(
    'https://api.bard.ai/v1/models/bard/generate',
    verify=False)


def get_response(prompt):
  """Gets a response from the Bard language model.

  Args:
    prompt: The prompt to ask the Bard language model.

  Returns:
    The response from the Bard language model.
  """

  response = requests.post(
      'https://api.bard.ai/v1/models/bard/generate',
      json={'prompt': prompt},verify=False)
  response.raise_for_status()
  return response.json()['generated_text']