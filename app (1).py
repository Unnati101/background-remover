import gradio as gr
from rembg import remove

    
        
def imrem(img):
    return remove(img)
            



app = gr.Interface(imrem, inputs="image", outputs="image")
    
app.launch(share=True)