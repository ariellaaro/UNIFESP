# input: sequência numérica
# output: maior e menor número, média, mediana e desvio padrão

#include  <stdio.h>
#include <math.h>

int main()
{
    int n;
    printf("Quantos números na sua série (N): ");
    scanf("%d", &n);
    float l[n];
    printf("Entre com números:\n");
    
    for(int i=0; i<n; i++){
        scanf("%f", &l[i]);
    }
    
///// MÍNIMO E MÁXIMO /////

    float max=l[0], min=l[0];
    
    for(int i=1; i<n; i++){
        if(min>l[i]) min=l[i];
    }
    
    for(int i=1; i<n; i++){
        if(max<l[i]){
            max=l[i];
        }
    }
    
///// MÉDIA /////
    
    float m=0, mm;
    
    for(int i=0; i<n; i++){
        m+=l[i];
    }
    
    mm=m/n;

///// MEDIANA /////
    float aaaa, md;
    
    for(int i=0; i<n; i++){
        for(int j=i+1; j<n; j++){
            if(l[j]<l[i]){
                aaaa = l[i];
                l[i] = l[j];
                l[j] = aaaa;
            }
        }
    }
    
    if(n%2==0){
        float medtemp=l[n/2-1]+l[n/2];
        md=medtemp/2;
    }
    else{
      md=l[n/2];
    }
    
///// DESVIO PADRÃO /////
    float dptemp=0, dp;
    
    for(int i=0; i<n; i++){
    dptemp+=(l[i]-mm)*(l[i]-mm);
    }
    
    dp=sqrt(dptemp/n); // usando os valores do ex dá 31, q eu conferi em uma calculadora online como sendo o dp populacional
                    // ent resolvi deixar assim msm apesar de no ex dar 33, q eu acho que é o dp amostral

///////////////////////////////////////////////////////////////////////////////////////////////////
    
    printf("Valor mínimo: %.2f\nValor máximo: %.2f\nMédia: %.2f\nMediana: %.2f\nDesvio padrão: %f", min, max, mm, md, dp)
    // no ex só o desvio padrão estava com todas as casas, ent resolvi arrendondar só o resto (p n ficar 3.000000000)
    
    
    return 0;
}
