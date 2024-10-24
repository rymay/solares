from exts import db


class Solares(db.Model):
    __tablename__ = 'Solares'
    idSolar = db.Column(db.Integer, primary_key=True)
    NombreFinca = db.Column(db.String(200))
    Calle = db.Column(db.String(150))
    nCalle = db.Column(db.String(5))
    Puerta = db.Column(db.String(5))
    Extension = db.Column(db.String(10))

    def __repr__(self):
            return f"<Solares {self.NombreFinca}"

    def save(self):
        db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, NombreFinca, Calle, nCalle, Puerta, Extension):
        self.NombreFinca = NombreFinca
        self.Calle = Calle
        self.nCalle = nCalle
        self.Puerta = Puerta
        self.Extension = Extension

        db.session.add(self)
        db.session.commit()

class Usuarios(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    usuario=db.Column(db.String(), nullable=False)
    contrasena=db.Column(db.String())
    NUsuario=db.Column(db.String())
    Delegacion=db.Column(db.String())
    SubDelegacion=db.Column(db.String())

    def __repr__(self):
        return f"<Usuarios {self.usuario}"

    def save(self):
        db.session.add(self)
        db.session.commit()
    
# class Ficheros(db.Model):
#     __tablename__ = 'FicherosSolares'
#     idFichero = db.Column(db.Integer, primary_key=True)
#     idSolar = db.Column(db.Integer,nullable=False)
#     Fichero = db.column(db.String(150))
#     NombreFichero = db.Column(db.String(50), nullable=False)
    
#     def __repr__(self):
#          return f"<FicherosSolares {self.NombreFichero}"
