import io
import datetime
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import FileResponse
from reportlab.pdfgen import canvas
from .models import Product
from .forms import ProductModelForm

# Create your views here.

class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product


class ProductCreate(CreateView):
    form_class = ProductModelForm
    model = Product
    success_url = reverse_lazy('products')


class ProductUpdate(UpdateView):
    form_class = ProductModelForm
    model = Product
    success_url = reverse_lazy('products')


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('products')


class Report(View):
    def get(self, request):
        buffer = io.BytesIO()
        pdf = canvas.Canvas(buffer)

        current_date = datetime.date.today()

        pdf.setTitle(f'report-{current_date}')
        pdf.setFont('Helvetica-Oblique', 14)
        pdf.drawString(220, 820, f'Relatório {current_date.strftime("%d/%m/%Y")}')

        y = 790
        pdf.setFont('Helvetica-Bold', 10)
        pdf.drawString(10, y, 'ID')
        pdf.drawString(80, y, 'Nome')
        pdf.drawString(300, y, 'Preço')
        pdf.drawString(420, y, 'Quantidade')
        pdf.line(10, y-5, 585, y-5)
        y = y - 20

        for product in Product.objects.all():
            if y <= 40:
                pdf.showPage()
                y = 790
            pdf.setFont('Helvetica', 10)
            pdf.drawString(10, y, f'{product.id}')
            pdf.drawString(80, y, f'{product.name}')
            pdf.drawString(300, y, f'R${product.price:.2f}')
            pdf.drawString(420, y, f'{product.quantity}')
            pdf.line(10, y-5, 585, y-5)
            y = y - 20

        pdf.showPage()
        pdf.save()

        buffer.seek(0)

        return FileResponse(buffer, as_attachment=True, filename=f'report-{current_date}.pdf')
