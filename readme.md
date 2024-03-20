# Picture creator

Creates a picture using stable diffusion 1.5<br>
Everything is configurable within the main file and environment variables

## Examples made with this code:
<img src="example1.jpeg" width="200" height="200" title="Pasta 1" alt="pasta 1">
<img src="example2.jpeg" width="200" height="200" title="Pasta 2" alt="pasta 2"><br>

## Existing editing features:
<table style="border:1px solid white; margin:auto; margin:auto; text-align:center;">
  <tr>
    <th>Normal</th>
    <th>Enhanced</th>
    <th>Grey scaled</th>
    <th>Negative</th>
    <th>Hide specific color</th>
  </tr>
  <tr>
    <td><img src="example3.png" width="100" height="100" title="Pasta" alt="pasta"></td>
    <td><img src="example4.png" width="100" height="100" title="Pasta" alt="pasta"></td>
    <td><img src="example5.png" width="100" height="100" title="Pasta" alt="pasta"></td>
    <td><img src="example6.png" width="100" height="100" title="Pasta" alt="pasta"></td>
    <td><img src="example7.png" width="100" height="100" title="Pasta" alt="pasta"></td>
  </tr>
</table>


## What you need to install to run this:
```shell
pip install diffusers transformers accelerate pillow
```

## How to run:
```shell
python main.py
```

## Where all models installed:
```
~/.cache/huggingface/hub
```

