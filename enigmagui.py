import tkinter as tk
from tkinter import ttk, messagebox

class Rotor:
    def __init__(self, wiring, notch):
        self.wiring = wiring
        self.notch = notch
        self.position = 0
        
    def forward(self, char):
        shift = (ord(char) - ord('A') + self.position) % 26
        after_wiring = self.wiring[shift]
        return chr((ord(after_wiring) - ord('A') - self.position) % 26 + ord('A'))
    
    def backward(self, char):
        shift = (ord(char) - ord('A') + self.position) % 26
        after_wiring = chr((self.wiring.index(chr(shift + ord('A'))) - self.position) % 26 + ord('A'))
        return after_wiring
    
    def rotate(self):
        self.position = (self.position + 1) % 26
        return self.position == self.notch

class Reflector:
    def __init__(self, wiring):
        self.wiring = wiring
    
    def reflect(self, char):
        return self.wiring[ord(char) - ord('A')]

class EnigmaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Mesin Enigma")
        
        # Konfigurasi warna
        self.colors = {
            'bg': '#2C3E50',
            'fg': '#ECF0F1',
            'frame_bg': '#34495E',
            'button_bg': '#2980B9',
            'button_fg': 'white',
            'entry_bg': '#ECF0F1',
            'entry_fg': '#2C3E50'
        }
        
        self.root.configure(bg=self.colors['bg'])
        
        # Style konfigurasi
        self.style = ttk.Style()
        self.style.configure('TLabel', 
            background=self.colors['frame_bg'],
            foreground=self.colors['fg'],
            font=('Arial', 10)
        )
        self.style.configure('TLabelframe', 
            background=self.colors['frame_bg']
        )
        self.style.configure('TLabelframe.Label', 
            background=self.colors['frame_bg'],
            foreground=self.colors['fg'],
            font=('Arial', 10, 'bold')
        )
        
        # Inisialisasi rotor dan reflector
        self.rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 'Q')
        self.rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", 'E')
        self.rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", 'V')
        self.reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Input Frame
        input_frame = ttk.LabelFrame(self.root, text="Input", padding="10", style='TLabelframe')
        input_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        
        ttk.Label(input_frame, text="Masukkan Teks:").grid(row=0, column=0, sticky="w")
        self.input_text = tk.Text(input_frame, height=5, width=40, 
            bg=self.colors['entry_bg'],
            fg=self.colors['entry_fg'],
            font=('Arial', 10)
        )
        self.input_text.grid(row=1, column=0, padx=5, pady=5)
        
        # Rotor Settings Frame
        settings_frame = ttk.LabelFrame(self.root, text="Pengaturan Rotor", padding="10", style='TLabelframe')
        settings_frame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        
        ttk.Label(settings_frame, text="Posisi Rotor (0-25):").grid(row=0, column=0, columnspan=3)
        
        self.rotor1_pos = ttk.Spinbox(settings_frame, from_=0, to=25, width=5)
        self.rotor2_pos = ttk.Spinbox(settings_frame, from_=0, to=25, width=5)
        self.rotor3_pos = ttk.Spinbox(settings_frame, from_=0, to=25, width=5)
        
        self.rotor1_pos.grid(row=1, column=0, padx=5)
        self.rotor2_pos.grid(row=1, column=1, padx=5)
        self.rotor3_pos.grid(row=1, column=2, padx=5)
        
        # Buttons
        button_frame = tk.Frame(self.root, bg=self.colors['bg'])
        button_frame.grid(row=2, column=0, pady=10)
        
        tk.Button(button_frame,
            text="Enkripsi",
            command=self.encrypt,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=('Arial', 10, 'bold'),
            width=10
        ).grid(row=0, column=0, padx=5)
        
        tk.Button(button_frame,
            text="Dekripsi",
            command=self.encrypt,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=('Arial', 10, 'bold'),
            width=10
        ).grid(row=0, column=1, padx=5)
        
        tk.Button(button_frame,
            text="Reset",
            command=self.reset,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=('Arial', 10, 'bold'),
            width=10
        ).grid(row=0, column=2, padx=5)
        
        # Output Frame
        output_frame = ttk.LabelFrame(self.root, text="Output", padding="10", style='TLabelframe')
        output_frame.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
        
        self.output_text = tk.Text(output_frame, height=5, width=40,
            bg=self.colors['entry_bg'],
            fg=self.colors['entry_fg'],
            font=('Arial', 10),
            state='disabled'
        )
        self.output_text.grid(row=0, column=0, padx=5, pady=5)
    
    def reset(self):
        self.input_text.delete(1.0, tk.END)
        self.output_text.config(state='normal')
        self.output_text.delete(1.0, tk.END)
        self.output_text.config(state='disabled')
        self.rotor1_pos.delete(0, tk.END)
        self.rotor2_pos.delete(0, tk.END)
        self.rotor3_pos.delete(0, tk.END)
        self.rotor1_pos.insert(0, "0")
        self.rotor2_pos.insert(0, "0")
        self.rotor3_pos.insert(0, "0")
    
    def encrypt(self):
        try:
            self.rotor1.position = int(self.rotor1_pos.get())
            self.rotor2.position = int(self.rotor2_pos.get())
            self.rotor3.position = int(self.rotor3_pos.get())
            
            text = self.input_text.get(1.0, tk.END).strip().upper()
            result = ""
            
            for char in text:
                if char.isalpha():
                    if self.rotor2.rotate():
                        self.rotor3.rotate()
                    if self.rotor1.rotate():
                        self.rotor2.rotate()
                    
                    c = self.rotor1.forward(char)
                    c = self.rotor2.forward(c)
                    c = self.rotor3.forward(c)
                    c = self.reflector.reflect(c)
                    c = self.rotor3.backward(c)
                    c = self.rotor2.backward(c)
                    c = self.rotor1.backward(c)
                    
                    result += c
                else:
                    result += char
            
            self.output_text.config(state='normal')
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(1.0, result)
            self.output_text.config(state='disabled')
            
        except ValueError:
            messagebox.showerror("Error", "Posisi rotor harus berupa angka antara 0-25")

if __name__ == "__main__":
    root = tk.Tk()
    app = EnigmaGUI(root)
    root.mainloop()