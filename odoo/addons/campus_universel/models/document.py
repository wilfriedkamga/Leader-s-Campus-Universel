from odoo import _, api, fields, models, tools

class ProcedureEtapeDocument(models.Model):
    
    _name = 'campus_universel.procedure.document'
    _description = 'Documents requis pour une étape'
    _table='cu_document'

    name = fields.Char(string='Nom du document')
    url = fields.Char(string='Lien externe')
    file  = fields.Binary()
    is_uploaded  = fields.Boolean(default=False)
    etape_id = fields.Many2one('campus_universel.procedure.etape', string='Étape')
    # Lien vers la procédure (Nouveau champ)
    procedure_id = fields.Many2one(
        'campus_universel.procedure',
        string="Procédure",
        compute='_compute_procedure',
        store=True
    )
    
    def _compute_procedure(self):
        """Récupérer la procédure associée à partir de l'étape"""
        for action in self:
            action.procedure_id = action.etape_id.procedure_id if action.etape_id else False
    
    provenance = fields.Selection([
    ('candidat', 'Fourni par le candidat'),
    ('procedure', 'Obtenu lors de la procédure')
    ], string='Provenance du document')

    category = fields.Selection([
        ('image', 'Image'),
        ('document', 'Document'),
        ('video', 'Vidéo'),
        ('audio', 'Audio'),
        ('archive', 'Fichier compressé'),
        ('other', 'Autre')
    ], string='Catégorie de fichier')

    extension = fields.Selection([
        ('pdf', 'PDF'),
        ('doc', 'Word (.doc)'),
        ('docx', 'Word (.docx)'),
        ('xls', 'Excel (.xls)'),
        ('xlsx', 'Excel (.xlsx)'),
        ('ppt', 'PowerPoint (.ppt)'),
        ('pptx', 'PowerPoint (.pptx)'),
        ('jpg', 'Image (.jpg)'),
        ('jpeg', 'Image (.jpeg)'),
        ('png', 'Image (.png)'),
        ('mp3', 'Audio (.mp3)'),
        ('mp4', 'Vidéo (.mp4)'),
        ('avi', 'Vidéo (.avi)'),
        ('zip', 'Fichier compressé (.zip)'),
        ('rar', 'Fichier compressé (.rar)'),
    ], string='Extension du fichier')

    url = fields.Char(string='Lien externe')

    @api.onchange('category')
    def _update_extensions(self):
        """ Met à jour les extensions en fonction de la catégorie sélectionnée """
        category_extensions = {
            'image': ['jpg', 'jpeg', 'png'],
            'document': ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx'],
            'video': ['mp4', 'avi'],
            'audio': ['mp3'],
            'archive': ['zip', 'rar'],
        }
        if self.category:
            extensions = category_extensions.get(self.category, [])
            if extensions:
                self.extension = extensions[0]  
            else:
                self.extension = False
