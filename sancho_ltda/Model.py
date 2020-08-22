from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
ma = Marshmallow()
db = SQLAlchemy()


class Paises(db.Model):
    __tablename__ = 'paises'
    pai_id = db.Column(db.Integer, primary_key=True)
    pai_nom = db.Column(db.String(256), nullable=False)

    def __init__(self, pai_nom):
        self.pai_nom = pai_nom


class Departamentos(db.Model):
    __tablename__ = 'departamentos'
    dep_id = db.Column(db.Integer, primary_key=True)
    dep_nom = db.Column(db.String(256), nullable=False)
    dep_pai_id = db.relationship('Paises', backref=db.backref('\
            departamentos', lazy=True))

    def __init__(self, dep_nom):
        self.dep_nom = dep_nom


class Ciudades(db.Model):
    __tablename__ = 'ciudades'
    ciu_id = db.Column(db.Integer, primary_key=True)
    ciu_nom = db.Column(db.String(256), nullable=False)
    ciu_dep_id = db.relationship('Departamentos', backref=db.backref('\
            ciudades', lazy=True))
    ciu_pai_id = db.relationship('Paises', backref=db.backref('\
            ciudades', lazy=True))

    def __init__(self, ciu_nom):
        self.ciu_nom = ciu_nom


class Categorias(db.Model):
    __tablename__ = 'categorias'
    cat_id = db.Column(db.Integer, primary_key=True)
    cat_nom = db.Column(db.String(256), nullable=False)

    def __init__(self, cat_nom):
        self.cat_nom = cat_nom


class Estados(db.Model):
    __tablename__ = 'estados'
    est_id = db.Column(db.Integer, primary_key=True)
    est_nom = db.Column(db.String(256), nullable=False)

    def __init__(self, est_nom):
        self.est_nom = est_nom


class Metodos(db.Model):
    __tablename__ = 'metodos'
    met_id = db.Column(db.Integer, primary_key=True)
    met_nom = db.Column(db.String(256), nullable=False)

    def __init__(self, met_nom):
        self.met_nom = met_nom


class Clientes(db.Model):
    __tablename__ = 'clientes'
    cli_ced = db.Column(db.Float, primary_key=True)
    cli_nom = db.Column(db.String(256), nullable=False)
    cli_dir = db.Column(db.String(256), nullable=False)
    cli_tel = db.Column(db.String(256), nullable=False)
    cli_fot = db.Column(db.String(256), nullable=False)
    cli_dep_id = db.relationship('Departamentos', backref=db.backref('\
            clientes', lazy=True))
    cli_pai_id = db.relationship('Paises', backref=db.backref('\
            clientes', lazy=True))
    cli_ciu_id = db.relationship('Ciudades', backref=db.backref('\
            clientes', lazy=True))

    def __init__(self, cli_nom):
        self.cli_nom = cli_nom


class Facturas(db.Model):
    __tablename__ = 'facturas'
    fac_id = db.Column(db.Integer, primary_key=True)
    fac_cli_ced = db.Column(db.Float, nullable=False)
    fac_fec = db.Column(db.Datetime(), nullable=False)
    fac_tot = db.Column(db.Float, nullable=False)
    fac_met_id = db.relationship('Metodos', backref=db.backref('\
            facturas', lazy=True))

    def __init__(self, fac_id):
        self.fac_id = fac_id


class Productos(db.Model):
    __tablename__ = 'productos'
    pro_id = db.Column(db.Integer, primary_key=True)
    pro_nom = db.Column(db.String(256), nullable=False)
    pro_pre = db.Column(db.Float, nullable=False)
    pro_inv = db.Column(db.Integer, nullable=False)
    pro_cat_id = db.relationship('Categorias', backref=db.backref('\
            productos', lazy=True))
    pro_est_id = db.relationship('Estados', backref=db.backref('\
            productos', lazy=True))

    def __init__(self, pro_nom):
        self.pro_nom = pro_nom


class Facturas_Productos(db.Model):
    __tablename__ = 'facturas_productos'
    fac_pro_id = db.Column(db.Integer, primary_key=True)
    fac_pro_fac_id = db.Column(db.Integer, nullable=False)
    fac_pro_pro_id = db.Column(db.Integer, nullable=False)
    fac_pro_can = db.Column(db.Integer, nullable=False)
    fac_pro_pre = db.Column(db.Float, nullable=False)

    def __init__(self, fac_pro_id):
        self.fac_pro_id = fac_pro_id
